import requests
from bs4 import BeautifulSoup
from holder.chapter import Chapter
from holder.info import Info
from holder.update import Update
from holder.search import Search
import re


class MangaPark:
    def __init__(self):
        self.__link_update = "http://mangapark.me"
        self.__lupdate = []

    def get_update(self):
        try:
            source_code = requests.get(self.__link_update).text
            soup = BeautifulSoup(source_code, "html.parser")
            text_raw = soup.find(name="div", attrs={"class": "bd ls1"})
            [text.extract() for text in text_raw.find_all(string="\n")]
            for n in text_raw.contents:
                tag_manga = BeautifulSoup(str(n.contents[0]), "html.parser")
                tag_link = self.__link_update + tag_manga.a["href"]
                tag_title = tag_manga.a["title"]
                tag_small_cover = tag_manga.img["src"]
                tag_chapter = BeautifulSoup(str(n.contents[1]), "html.parser").find_all(name="li")
                lchapter = []
                for m in tag_chapter:
                    tagch_link = self.__link_update + m.a["href"]
                    tagch_title = m.a.text
                    tagch_time = m.i.text
                    dt = Chapter(tagch_link, tagch_title, tagch_time)
                    lchapter.append(dt)
                data = Update(tag_title, tag_small_cover, lchapter, tag_link)
                self.__lupdate.append(data)
            return self.__lupdate
        except:
            return None

    def get_info(self, update=None):
        try:
            lchapter = []
            source_code = requests.get(update.link).text
            soup = BeautifulSoup(source_code, "html.parser")

            text_chapter = soup.find_all(name="div", attrs={"class": "stream"})
            while len(text_chapter) == 0:
                source_code = requests.get(update.link).text
                soup = BeautifulSoup(source_code, "html.parser")

                text_chapter = soup.find_all(name="div", attrs={"class": "stream"})
                if text_chapter != 0:
                    break
            soupchapter = BeautifulSoup(str(text_chapter), "html.parser")
            try:
                [text.extract() for text in soupchapter.find_all("div", {"class": "stream collapsed"})]
                text_chapter = soupchapter.find(name="div", attrs={"class": "stream"}).contents[3].contents[3]
            except:
                text_chapter = soupchapter.find(name="div", attrs={"class": "stream"})
            soupchapter = BeautifulSoup(str(text_chapter), "html.parser")
            text_chapter = soupchapter.find_all(name="li")
            for n in text_chapter:
                ch_text = self.__clean_atribute(n.contents[1].text)
                ch_link = self.__link_update + n.contents[1].a["href"][0:-2]
                dt = Chapter(ch_link, ch_text)
                lchapter.append(dt)
            text_raw = soup.find(name="section", attrs={"class": "manga"})
            del soup
            del soupchapter

            soup_in = BeautifulSoup(str(text_raw), "html.parser")

            temp = soup_in.find(name="p", attrs={"class": "summary"})
            summary = "Not Found!"
            if temp is not None:
                summary = self.__clean_atribute(temp.text)

            text_in = soup_in.find(name="div", attrs={"class": "hd"})
            title = text_in.contents[1].text

            text_in = soup_in.find(name="div", attrs={"class": "cover"})
            cover = text_in.img["src"]

            text_in = soup_in.find(name="table", attrs={"class": "attr"})
            soup_table = BeautifulSoup(str(text_in), "html.parser").find_all(name="tr")

            rating = re.search("Average.*total votes", soup_table[1].td.text).group()
            rank = re.search("[0-9].*views", soup_table[2].td.text).group()
            alternative = self.__clean_atribute(soup_table[3].td.text)
            author = self.__clean_atribute(soup_table[4].td.text)
            artist = self.__clean_atribute(soup_table[5].td.text)
            genre = self.__clean_atribute(soup_table[6].td.text)
            typemanga = self.__clean_atribute(soup_table[7].td.text)
            release = soup_table[8].td.text
            status = self.__clean_atribute(soup_table[9].td.text)

            infomanga = Info(title, rating,
                             rank, alternative,
                             author, artist,
                             genre, typemanga,
                             release, status,
                             cover, summary, lchapter)
            return infomanga
        except:
            return None

    def get_image(self, chapter):
        llink = []
        source_code = requests.get(chapter.link).text
        soup = BeautifulSoup(source_code, "html.parser")
        text_view = soup.find_all(name="div", attrs={"class": "canvas"})
        for n in text_view:
            llink.append(n.contents[3].img["src"])
        return llink

    def __clean_atribute(self, text=None):
        text = str.replace(text, "\t", "")
        text = str.replace(text, "\n", "")
        text = str.replace(text, "\r", "")
        text = str.replace(text, "  ", "")
        return text

    def get_num_page(self):
        r = requests.get("http://mangapark.me/search?q&orderby=a-z")
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.find_all(name="ul", attrs={"class": "paging full"})[0]
        b = a.contents[len(a.contents) - 6].text
        return int(b[3:6])

    def get_search(self, num):
        searchresult = []
        r = requests.get("http://mangapark.me/search?q&orderby=a-z&page=" + str(num))
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        mainTable = soup.find(name="div", attrs={"class": "manga-list"})
        items = mainTable.find_all(name="div", attrs={"class": re.compile("item")})
        for item in items:
            src = Search()
            tditem = item.find_all(name="td")
            src.link = tditem[0].a["href"]
            src.title = tditem[0].a["title"]
            src.pic = tditem[0].img["src"]
            src.rate = tditem[1].div.i.text

            inforad = tditem[1].find(name="div", attrs={"class": "info radius"})
            fields = inforad.find_all(name="div", attrs={"class": re.compile("field")})
            for field in fields:
                res, st = self.get_field_extract(str(field))
                if st == 1:
                    src.altern = res  # alternat
                elif st == 2:
                    src.author = res[0:len(res) - 2]
                    src.stat = res[len(res) - 2]
                    src.relase = res[len(res) - 1]
                elif st == 3:
                    src.genre = res

            searchresult.append(src)
        return searchresult

    def get_field_extract(self, string):
        st = -1
        field = BeautifulSoup(string, "html.parser")
        if field.b.text == "Alternative:":
            st = 1
            txt = field.contents[0]
            # aku butuh claning text
            return txt, st
        else:
            returnlist = []
            for a in field.find_all(name="a"):
                returnlist.append(a.text)
            if field.b.text == "Authors/Artists:":
                st = 2
            else:
                st = 3
            return returnlist, st
