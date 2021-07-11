import pandas as pd
import matplotlib.pyplot as plt

#Loading the data from a csv into a pandas dataframe
Banned_Maps = pd.read_csv("Data/banned_maps_stats.csv")
Maps_picked = pd.read_csv("Data/map_pick_stats.csv")
Player_Stats = pd.read_csv("Data/player_stats.csv")
CTorTsided = pd.read_csv("Data/side_pick_stats.csv")
#Declaring a list for all participating countries
Countries = ["Canada", "Belgium", 'United States',' United Kingdom', 'Finland', "South Korea", "Thailand", "Japan", "Czech Republic", "Croatia", "Chile", "Brazil", "Argentina"]

def MBLineGraph():
    figure = plt.figure()
    plt.plot(Banned_Maps.loc[:,'Map'], Banned_Maps.loc[:,'Total'])
    plt.title('Valorant Masters 2021 - Maps Banned')
    plt.show()

def MBPBarGraph():
    figure = plt.figure()
    plt.bar(Banned_Maps.loc[:,'Map'], Banned_Maps.loc[:,'Total'])
    plt.title('Valorant Masters 2021 - Maps Banned')
    plt.show()

def PlayerCountryBased():
    for i in range(len(Countries)):
        row = Player_Stats[Player_Stats["Country"] == Countries[i]].sort_values(by="KDA", ascending=False).head()
        Best = row[0:1]
        Country = Countries[i]
        Player = str(Best["Player"].to_string())
        KDA = str(Best["KDA"].to_string())
        return("The best Player from " + Country + " is " + Player + ", with a KDA of " + KDA)

def KDACountryBased():
    for i in range(len(Countries)):
        Countryed_DF = Player_Stats[Player_Stats["Country"] == Countries[i]]
        for index, row in Countryed_DF.iterrows():
            KDALIST = []
            KDALIST.append(row["KDA"])
        Total = sum(KDALIST)
        AverageOfCountry = Total/len(KDALIST)
        return("- The Country " + Countries[i] + " has an average of a "+ str(AverageOfCountry) + " KDA")

#PlayerCountryBased()
#KDACountryBased()
MBPBarGraph()
#MBLineGraph()



