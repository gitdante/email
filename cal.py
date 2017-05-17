from osgeo import gdal
import numpy as np
import os
import re

def readdata(f):
    fid = gdal.Open(f, gdal.GA_ReadOnly)
    data = fid.GetRasterBand(1).ReadAsArray()
    return data

def cal8daysum(l):
    start=1
    end=1
    cal8 = []
    l = np.array(l)
    while end!=121:
        end += 8
        cal8.append(np.sum(l[start:end,:,:],axis=0))
        start=end
    cal8=np.array(cal8)
    return cal8

def writetif(l):
    fid1 = gdal.Open(files[0], gdal.GA_ReadOnly)
    prj = fid1.GetProjection()
    geo = fid1.GetGeoTransform()
    lat = fid1.GetRasterBand(1).ReadAsArray()
    dims = np.shape(lat)
    driver = gdal.GetDriverByName('GTiff')
    for i in range(15):
        ds = driver.Create('8'+files[i], dims[1], dims[0], 1, gdal.GDT_Float32)
        ds.SetGeoTransform(geo)
        ds.SetProjection(prj)
        band = ds.GetRasterBand(1)
        band.WriteArray(l[i,:,:])
        ds.FlushCache()
    return 'done'

files = os.listdir('./')
files = filter(lambda x:'.tif' in x,files)
a =[]
for i in files:
    a.append(readdata(i))
b = cal8daysum(a)
print  b.shape
writetif(b)
