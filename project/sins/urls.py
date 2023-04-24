from django.urls import path
from . views import admin
from . views import users, tambahUser, postDatauser, updateDatauser, postUpdateuser, deleteDatauser, postDeleteuser
from . views import guru , tambahGuru, detailGuru, updateDataGuru, deleteDataGuru, postDeleteGuru
from . views import kelas, tambahKelas, updateDatakelas, deleteDataKelas, postDeleteKelas, detailKelas
from . views import mapel, tambahMapel, updateDataMapel, deleteDataMapel, postDeleteMapel
from . views import siswa , tambahSiswa, detailSiswa, updateDataSiswa, deleteDataSiswa, postDeleteSiswa
from . views import siswakelas
urlpatterns = [
   # path('',index,name='index'),
   
   
   path('admin',admin, name="admin"),

   # Url For admin/user page
   path('indexUsers',users, name="indexusers"),
   path('tambahUser', tambahUser, name="tambahuser"),
   path('postDatauser', postDatauser, name="postdatauser"),
   path('updateDatauser/<str:id_user>', updateDatauser, name="updatedatauser"),
   path('postUpdateuser', postUpdateuser, name="postupdatedatauser"),
   path('deleteDatauser/<str:id_user>', deleteDatauser, name="deletedatauser"),
   path('postDeleteuser/<str:id_user>', postDeleteuser, name="postdeleteuser"),

   # Url For admin/guru page
   path('indexGuru', guru, name="indexguru"),
   path('tambahGuru', tambahGuru, name="tambahguru"),
   path('detailGuru/<str:nip>', detailGuru, name="detailguru"),
   path('updateDataGuru/<str:nip>', updateDataGuru, name="updatedataguru"),
   path('deleteDataGuru/<str:nip>', deleteDataGuru, name="deletedataguru"),
   path('postDeleteGuru/<str:nip>', postDeleteGuru, name="postdeleteguru"),

   #Url For admin/kelas page
   path('indexKelas',kelas, name="indexkelas"),
   path('tambahKelas', tambahKelas, name="tambahkelas"),
   path('updateDatakelas/<str:id_kelas>',updateDatakelas, name="updatedatakelas"),
   path('deleteDatakelas/<str:id_kelas>',deleteDataKelas, name="deletedatakelas"),
   path('postDeleteKelas/<str:id_kelas>',postDeleteKelas, name="postdeletekelas"),
   # path('mapelKelas/<str:id_kelas>',mapelKelas, name="mapelkelas"),
   path('detailKelas/<str:id_kelas>',detailKelas, name="detailkelas"),

   #Url For admin/mapel page
   path('indexMapel', mapel, name="indexmapel"),
   path('tambahMapel',tambahMapel, name="tambahmapel"),
   path('updateDataMapel/<str:id_mapel>', updateDataMapel, name="updatedatamapel"),
   path('deleteDataMapel/<str:id_mapel>', deleteDataMapel, name="deletedatamapel"),
   path('postDeleteMapel/<str:id_mapel>', postDeleteMapel, name="postdeletemapel"),

   #Url For admin/siswa page
   path('indexSiswa', siswa, name="indexsiswa"),
   path('tambahSiswa', tambahSiswa, name="tambahsiswa"),
   path('detailSiswa/<str:nis>', detailSiswa, name="detailsiswa"),
   path('updateDataSiswa/<str:nis>', updateDataSiswa, name="updatedatasiswa"),
   path('deleteDataSiswa/<str:nis>', deleteDataSiswa, name="deletedatasiswa"),
   path('postDeleteSiswa/<str:nis>', postDeleteSiswa, name="postdeletesiswa"),

   path('siswakelas',siswakelas, name="siswakelas")
]