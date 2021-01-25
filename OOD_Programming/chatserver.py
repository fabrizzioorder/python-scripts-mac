'''
Chat Server

Explain how you would design a chat server.
Provide details about the various backend components, classes, and methods.
What would be the hardest problems to solve?

Core Functionality:
    Adding a user
    creating a conversation
    updating ones status
    group chats and one-on-ones

Actions:
    Singing on and offline
    add requests (sending, accepting, and rejecting)
    updating a status message
    creating private and group chats
    adding new messages to private and group chats

How to implement?
    Most likely will consist:
        Database
            - used for permanant storage such as user list or chat achives
            - SQL database is a good bet (potentially BigTable for more scalability)
        Communication between client and servers
            - XML will work well (easy for both humans and computers to read)
            - not most compressed format, but will help in debugging
        Server
            - data will be split accross a set of machines
            - try to replicate some data across machines to minimize lookup
            - dont have ONE machine be responsible for storing all user sign ins

'''