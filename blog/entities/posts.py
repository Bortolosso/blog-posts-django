class Posts():
    def __init__(self, tittle, slug, author, content, status):
        self.__tittle = tittle
        self.__slug = slug
        self.__author = author
        self.__content = content
        self.__status = status

    @property
    def tittle(self):
        return self.__tittle
    
    @tittle.setter
    def tittle(self, tittle):
        self.__tittle = tittle

    @property
    def slug(self):
        return self.__slug
    
    @slug.setter
    def slug(self, slug):
        self.__slug = slug
    
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def content(self):
        return self.__content
    
    @content.setter
    def content(self, content):
        self.__content = content
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = status