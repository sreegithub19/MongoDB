# MongoDB
    # Video <a href="https://www.youtube.com/watch?v=E-1xI85Zog8&t=358s">link</a>
    # code: https://github.com/mikeckennedy/mongodb-quickstart-course
    # to get the code: git clone https://github.com/mikeckennedy/mongodb-quickstart-course.git
    # https://www.mongodb.com/try/download/community - to download mongodb
    # Commands to run mongodb:
    #     tar xzf mongodb-macos-x86_64-4.4.6.tgz
    #     sudo mv mongodb-macos-x86_64-4.4.6 /usr/local/mongodb
    #     cd /usr/local/mongodb
    #     sudo mkdir -p /System/Volumes/Data/data/db
    #   (below 2 commands to be run everytime for starting mongodb)
    #           sudo chown -R `id -un` /System/Volumes/Data/data/db
    #           sudo mongod --dbpath /System/Volumes/Data/data/db   # equivalent to 'mongod'(mongo daemon) command
    #      Now, in another terminal, type mongo:
    #           commands run here:
    #                show dbs -> shows databases
    #                exit -> to exit form mongo console
    #     now, go to bash profile from home directory :
    #               ls -al ; open .bash_profile
    #               type in .bash_profile:
    #                       export MONGO_PATH=/usr/local/mongodb
    #                       export PATH=$PATH:$MONGO_PATH/bin
    #               source .bash_profile -> to reload the bash file
    #
    # Commands to run the mongodb project:
    #       go into snake_bnb
    #       python3 -m venv .env --copies
    #       ls -ah
    #       source .env/bin/activate   (to activate the virtual environment in mac and linux)
    #               mypthon\Scripts\activate (in windows)
    #       pip install -r requirements.txt
    #       cd src  -> python3 program.py ->
    #                       ([g]uest or [h]ost) : g -> register_account,login,book a cage etc.
    #                                           : h -> register,login, register cage, list cages , add available date for cages, view bookings etc.
    #       go to src->data->mongodb.py
    #       modify program.py ; snakes.py; cages.py; bookings.py
    #       to check mongodb db's info:
    #            mongo -> show dbs -> use <db_name> -> show collections -> db.<collection_name>.find()  #collections: cages,owners,snakes
    #                               (with some condition): db.snakes.find({name:"viper"})
    #       once snake collection has been created in snake_bnb database, check it with db.snakes.find()
    # whoami - to get your username
    # mongo -version -> to show mongo version
    # pwd - present working directory
    # https://github.com/MongoEngine/mongoengine  - ODM (Object Document Mapper) for mongodb

