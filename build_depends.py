import os
import servbuild_setup as se

if se.FFMPEG_INSTALL and os.path.exists(se.DEPENDS_PATH+"/ffmpeg"):
    os.system("./"+se.DEPENDS_PATH+"/ffmpeg/"+se.FFMPEG_NAME+"/configure --disable-yasm --enable-static --libdir="+se.GIT_PATH_DOWNLOAD+"/3rdparty/ffmpeg/lib --shlibdir="+se.GIT_PATH_DOWNLOAD+"/3rdparty/ffmpeg/lib --incdir="+se.GIT_PATH_DOWNLOAD+"/3rdparty/ffmpeg/include")
    os.system("make -f "+se.DEPENDS_PATH+"/ffmpeg/"+se.FFMPEG_NAME+"/Makefile")
    os.system("sudo make install -f "+se.DEPENDS_PATH+"/ffmpeg/"+se.FFMPEG_NAME+"/Makefile")
