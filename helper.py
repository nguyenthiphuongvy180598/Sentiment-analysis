import os

ROOT = os.path.abspath(".")


class Helper:
    @staticmethod
    def read_text_file(file_path, encoding="utf-8", is_readlines=False):
        """
        Read the data in the text file

        :param file_path: the path of the file
        :param encoding: encoding for reading file
        :param is_readlines: return the whole text or list of lines of text file
        :return: text or list read from file
        """
        with open("%s/%s" % (ROOT, file_path), "r+", encoding=encoding) as f:
            if is_readlines:
                text = [t.replace("\n", "") for t in f.readlines()]
            else:
                text = f.read().replace("\n", "")
        return text

    @staticmethod
    def duplicate_terms_list(text=[]):
        result = []
        for t in text:
            if t.find(" ") >= 0:
                result.append(t.replace(" ", "_"))
            else:
                result.append(t)
        return result
