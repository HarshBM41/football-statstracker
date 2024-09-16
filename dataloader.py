from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="./SoccerNet/")
mySoccerNetDownloader.password = "XXXXXX" # Get this after filing the NDA form by SoccerNet
mySoccerNetDownloader.downloadDataTask(task="tracking", split=["train","test","challenge"])

# Optional, Originally meant for the 2023 challange of the community.
# I however am thinking of using this dataset as the base for the next step, for transforming the dataset into one that has ready trackID and labels
# for 3 classes, player, ball (and to be figured out) referee. This would minimze the need to restructure original labels separtaely for tracking players
# vs using different processes to handle team-realted metrics like possession rates.
mySoccerNetDownloader.downloadDataTask(task="tracking-2023", split=["train", "test", "challenge"]) 