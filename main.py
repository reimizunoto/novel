from src import bigee, tadu

if __name__ == '__main__':
    novel_name = input("Enter the name of the novel: ")
    novel = tadu.Tadu(novel_name)
    novel.download()