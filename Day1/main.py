import sys
class Grep:
    def open_file(self,filename:str):
        enc = 'utf-8'
        try:
            f=open(filename,"r",encoding=enc)
            return f 
        except:
            print(f"File {filename} does not exist")
        return -1
        
    def get_string_list(self) -> list[str]:
        self.Lines:list[str]=[]

        filenames = sys.argv[1:]
        for infile in filenames:
            f=self.open_file(infile)
            if(f == -1):
                continue
            for line in f:
                self.Lines.append(line)
            f.close()
        return self.Lines

    def print_map(self,map:dict[str:int]) -> None:
        for key in map:
            if key !='\n':
                print(f"There are {map[key]} {key}'s in the string")

    def stringcount(self,List:list[str]) -> dict[str:int]:
        count:dict[str:int] = {}
        for string in List:
            for letter in string:
                if letter in count:
                    count[letter] += 1
                else:
                    count[letter] = 1
        return count

    def __init__(self):
        self.string_list = []
        self.returned_count:dict[str:int] = {}

        string_list = self.get_string_list()
        returned_count = self.stringcount(string_list)
        self.print_map(returned_count)

    def line_count(self)->int:
        '''
        This funtion will return empty if called before get_string_list
        '''
        return len(self.Lines)


class Main:
    if __name__ == "__main__":
        import time
        start_time=time.time()
        g=Grep()
        print(g.line_count())
        print(f"The runtime of this program was {time.time()-start_time} seconds")