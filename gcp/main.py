'''
Dummy function to test GCP functionality 
'''

import base64
import pandas as pd
from mod_1 import ts


def timenow(event, context):
    '''
    Function creates a csv file with timestamp
    
    Output:
        Returns a csv file
    '''
    
    #import pandas as pd
    
    print("""This Function was triggered by messageId {} published at {}
    """.format(context.event_id, context.timestamp))
    
    d= {"Time": pd.Timestamp.now()}
    
    d = ts()
    
    print("Test if ts worked", d)
    
    df = pd.DataFrame(data=d, index=range(1))

    df.to_csv("/tmp/test_gcp.csv", index=False)
    
    print("Generated csv")
    
    


#if __name__ == "__main__":
#    d = ts()
    
#    df = pd.DataFrame(data=d, index=range(1))

 #   df.to_csv("/tmp/test_gcp.csv", index=False)
    
  #  print("Generated csv")
