from src import bigee, dushuge

if __name__ == '__main__':
    novel_name = input("Enter the name of the novel: ")
    novel = bigee.Bigee(novel_name)
    novel.download()