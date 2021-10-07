def isEven(ad):
    return int(ad)%2==0

def getTotalAds(batch):
    total_ads = 0
    for brand_ads in batch:
        if isEven(brand_ads):
            total_ads += int(brand_ads)
    return total_ads
batch = str(input())
print(getTotalAds(batch))
