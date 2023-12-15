# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:44:51 2023

@author: dell
"""

import pandas as pd

def main():
    df = pd.read_csv("titles.csv",)
        
    
    def getVowelsCount(columns):
        titles = str(columns["title"])
       
        count = 0
        vowels = ["a", "e", "i", "o", "u"]
    
        for i in range(len(titles)):
            if titles[i] in vowels:
                count = count + 1
            
        return (count)
    
                
    result = df.apply(getVowelsCount, axis=1, raw=False, result_type=None)
    
    df['vowels'] = result
    
    print(df)


if __name__ == "__main__":
    main()

