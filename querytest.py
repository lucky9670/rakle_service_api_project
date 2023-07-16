user_location = Point(lon, lat, srid=4326)
    
queryset = StoreInfo.objects.annotate(distance=Distance('location', user_location) / 1000).filter(distance__lt=radius).order_by(Distance('location', user_location) / 1000).values('StoreID', 'distance')