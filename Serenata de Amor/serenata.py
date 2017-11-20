from serenata_toolbox.datasets import Datasets
datasets = Datasets('Serenata/data/')

# now lets see what are the latest datasets available
for dataset in datasets.downloader.LATEST:
    print(dataset)  # and you'll see a long list of datasets!

# and let's download one of them
datasets.downloader.download('2016-12-06-reibursements.xz')  # yay, you've just downloaded this dataset to data/

# you can also get the most recent version of all datasets:
latest = list(datasets.downloader.LATEST)
datasets.downloader.download(latest)
