# session authentication

  client <--forbidden/unauthorised--|
   |                                |
   |                          wrong-credentials 
   |                                |
  \|/                               |
client ---username:password---> server 
                                    |
                                    |
                             right-credentials
                                    |
                             create-session-object
                                    |
  client <----session:id------------|
   |  
   |---------------------------|   
   |--request-header-----------|
   |      |                    |
   |      |--cookies           |----> server
   |           |--:session-id  |
   |                           |
   |--request-body-------------|
