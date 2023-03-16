import pandas as pd
import matplotlib.pyplot as plt

class Data():
    def __init__(self):
        self.data = pd.read_csv('c:/EmilyVolkova/2kurs/OPLabs/MyLabs/4Lab/exams.csv')

    def Dupl(self):
        self.data = self.data.drop_duplicates()

    def Uniq(self):
        for i in self.data:
            u = self.data[i].unique()
            print(u, str(len(u)))
        
    def Calcul(self):
        M = [
            self.data['math score'].min(), 
            self.data['math score'].max(), 
            self.data['math score'].mean(), 
            self.data['math score'].median()
            ]
        R = [
            self.data['reading score'].min(), 
            self.data['reading score'].max(), 
            self.data['reading score'].mean(), 
            self.data['reading score'].median()
            ]
        W = [
            self.data['writing score'].min(), 
            self.data['writing score'].max(), 
            self.data['writing score'].mean(), 
            self.data['writing score'].median()
            ]

        print(M)
        print(R)
        print(W)

    def Group(self):
        Gdata = self.data.groupby('race/ethnicity').agg({'math score': ['mean'], 'reading score': ['mean'], 'writing score': ['mean']}).reset_index()
        Gdata.columns = ['race/ethnicity', 'math score mean', 'reading score mean', 'writing score mean']
        SGdata = Gdata.sort_values(['math score mean', 'reading score mean', 'writing score mean'])
        print(SGdata)
        SGdata.hist()
        plt.show()

    def FiltrCalculHist(self):
        qual_col = ['high school']
        result_data = self.data[self.data['parental level of education'].isin(qual_col)].reset_index()

        mean_data = result_data.groupby('parental level of education').agg({'math score': ['mean'], 'reading score': ['mean'], 'writing score': ['mean']})
        mean_data.columns = ['math score mean', 'reading score mean', 'writing score mean']
        print(mean_data)
        mean_data['math score mean'].hist()
        mean_data['reading score mean'].hist()
        mean_data['writing score mean'].hist()
        plt.show()

    def Hist(self):
        df = pd.DataFrame(
            {
                'name column': ['math score', 'reading score', 'writing score'],
                'min': [self.data['math score'].min(), self.data['reading score'].min(), self.data['writing score'].min()], 
                'max': [self.data['math score'].max(), self.data['reading score'].max(), self.data['writing score'].max()],
                'sred': [self.data['math score'].mean(), self.data['reading score'].mean(), self.data['writing score'].mean()],
                'median': [self.data['math score'].median(), self.data['reading score'].median(), self.data['writing score'].median()]
            }
        )
        print(df)
        df.plot()
        plt.show()
        

BaseData = Data()
BaseData.Dupl()
BaseData.Uniq()
BaseData.Calcul()
BaseData.Group()
BaseData.FiltrCalculHist()
BaseData.Hist()

