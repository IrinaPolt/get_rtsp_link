def get_link(camera_name, username, password, IP, rtsp_port):
    rtsp_dict = {
    '3S': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/cam1/h264',
    '4XEM': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/live.sdp',
    'A-MTK': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/media/media.amp',
    'ABS': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4/1/media.amp',
    'Absolutron': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/image.mpg',
    'Acumen': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpg4/rtsp.amp',
    'Airlink101': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4',
    'AirLive': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/video.mp4',
    'ALinking': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/cam1/mjpeg',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/cam1/mpeg4',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/cam1/h264'
        ],
    'ALLIEDE': f'rtsp://{username}:{password}@{IP}:555/0/1:1/main',
    'Asante': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/cam1/mpeg4',
    'Asoni': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/GetData.cgi',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/'
        ],
    'Aviosys': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4',
        f'rtsp://{username}:{password}@{IP}:8554/mpeg4'
        ],
    'AVS Uriel': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4',
    'AVTech': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/live/mpeg4',
    'AVTech': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/live/h264',
    'AXIS': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4/media.amp',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/axis-media/media.amp'
        ],
    'AXview': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'Basler': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/h264?multicast',
    'BiKal IP CCTV': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/user.pin.mp2'
        ],
    'BlueJay': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4',
    'Bosch': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/rtsp_tunnel',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/video',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/?inst=2'
        ],
    'Brickcom': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/channel1',
    'Canon': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/stream/profile1=u',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/profile1=r',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/profile1=u'
        ],
    'CBC-Ganz': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/gnz_media/main',
    'Cisco': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/img/media.sav',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/'
        ],
    'Clairvoyant MWR': 'rtsp://{username}:{password}@{IP}:{rtsp_port}/av0_0',
    'CNB': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4'
        ],
    'Cohu': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/stream1',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/cam'
        ],
    'Compro': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/medias1',
    'Dahua': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/cam/realmonitor?channel=1&subtype=1',
    'D-Link': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/play1.sdp',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/play2.sdp'
        ],
    'Dallmeier': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/encoder1',
    'DoOurBest': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/ch0_0.h264',
    'DVTel-IOimage': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/ioImage/1',
    'EagleVision': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/11',
    'EDIMAX': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/ipcam.sdp',
        f'rtsp:/{username}:{password}@{IP}:{rtsp_port}/ipcam_h264.sdp'
        ],
    'ENEO': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/1/stream1',
    'Etrovision': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/rtpvideo1.sdp',
    'EverWorldView': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'EverFocus': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/streaming/channels/0',
    'Fine CCTV': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4',
    'FLIR Systems': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/ch0',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/vis',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/wfov'
        ],
    'Foscam': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/11',
    'FSAN': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'Gadspot': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/video.mp4',
    'Genie': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'Genius': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/avn=2',
    'GeoVision': f'rtsp://{username}:{password}@{IP}:8554/CH001.sdp',
    'Grandstream': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'GRUNDIG': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/jpeg',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/h264'
        ],
    'GVI': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4',
    'Hikvision': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/h264',
    'HuntElectronics': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/video1+audio1',
    'Ikegami': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/stream1',
    'iLink': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'IndigoVision': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'Infinova': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/1.AMP',
    'InnovativeSecurityDesigns': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/stream1',
    'INSTEK DIGITAL': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'Intellinet': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/video.mp4',
    'Intellio': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'IONodes': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/videoinput_1/h264_1/media.stm',
    'IPUX': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4',
    'IPx': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/camera.stm',
    'IQinVision': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/now.mp4',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mp4'
        ],
    'IRLAB': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'JVC': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/PSIA/Streaming/channels/0',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/PSIA/Streaming/channels/1'
        ],
    'KARE CSST-DIT': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'KTC': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/h264/',
    'Launch': f'rtsp://{IP}:{rtsp_port}/0/{username}:{password}/main',
    'Laview': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'LevelOne': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/access_code/',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/channel1'
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/live.sdp',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/video.mp4',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/h264'
        ],
    'Linksys': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/img/video.sav',
    'Logitech': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/HighResolutionVideo',
    'Lorex': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/video.mp4',
    'Lumenera': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'LUXONVIDEO': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/user_defined',
    'Marmitek': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4',
    'MaxVideo': f'rtsp://{IP}:{rtsp_port}/0/{username}:{password}/main',
    'MC Electronics': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'MeritLi-Lin': [
        f'http://{username}:{password}@{IP}:{rtsp_port}/rtsph264720p', # работает ли логин и пароль с http адресом?
        f'http://{username}:{password}@{IP}:{rtsp_port}/rtsph2641080p',
        f'http://{username}:{password}@{IP}:{rtsp_port}/rtsph264',
        f'http://{username}:{password}@{IP}:{rtsp_port}/rtsph2641024p',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/rtsph264',
        f'http://{username}:{password}@{IP}:{rtsp_port}/rtspjpeg',
        f'http://{username}:{password}@{IP}:{rtsp_port}/rtsph264'
        ],
    'MESSOA': [
        f'rtsp://{username}:{password}@{IP}:8557/h264',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/livestream/',
        f'rtsp://{username}:{password}@{IP}:7070/',
        ],
    'MicroDigital': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/cam0_0',
    'Moxa': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/multicaststream',
    'MultiPix': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/video1',
    'Onix': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/cam0_0',
    'OpenEye': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/h264',
    'Panasonic': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}//nphMpeg4/g726-640x48',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/nphMpeg4/g726-640x480',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/nphMpeg4/nil-320x240',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/MediaInput/h264',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/nphMpeg4/g726-640x',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/MediaInput/mpeg4'
        ],
    'Pelco': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/stream1',
    'PiXORD': f'rtsp://{username}:{password}@{IP}:{rtsp_port}',
    'Planet': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/ipcam.sdp',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/ipcam_h264.sdp',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/media/media.amp'
        ],
    'PRIME': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/cam1/h264/multicast',
    'QihanTechnology': f'rtsp://{username}:{password}@{IP}:{rtsp_port}',
    'Repotec': f'rtsp://{IP}:{rtsp_port}/cam1/mpeg4?user="{username}"&pwd="{password}"',
    'SafeSky': f'rtsp://{username}:{password}@{IP}:{rtsp_port}',
    'Samsung': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4unicast',
    'Samsung': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mjpeg/media.smp',
    'Samsung': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/h264/media.smp',
    'Sanan': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'Sanyo': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/VideoInput/1/h264/1',
    'ScallopImaging': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/main', # порт 8554
    'Sentry': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4',
    'SeyeonTech': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/cam0_1',
    'Sharx': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/live_mpeg4.sdp',
    'Siemens': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/img/video.asf',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/livestream'
        ],
    'Siqura': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/h264',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/VideoInput/1/h264/1',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/VideoInput/1/mpeg4/1'
        ],
    'Sitecom': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/img/video.sav',
    'Sony': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/media/video1',
    'Sparklan': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4',
    'Speco': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'StarDot': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/nph-h264.cgi',
    'StoreNet': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/stream1',
    'SuperCircuits': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/ch0_unicast_firststream',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/ch0_unicast_secondstream',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/live/mpeg4'
        ],
    'Swann': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4',
    'TCLINK': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/av2',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/live.sdp'
        ],
    'Topica': [
        f'rtsp://{username}:{password}@{IP}:7070/',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/h264/media.amp'
        ],
    'TP-Link': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/video.mp4',
    'TRENDnet': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/play1.sdp'
        ],
    'Truen': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/video1',
    'Ubiquiti': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/live/ch00_0',
    'UDP Technology': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/ch0_unicast_firststream',
    'Verint': f'rtsp://{username}:{password}@{IP}:{rtsp_port}',
    'Vgsion': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/11',
    'Vicon': [
        f'rtsp://{username}:{password}@{IP}:7070/',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/access_name_for_stream_1_to_5'
        ],
    'VICON': f'rtsp://{username}:{password}@{IP}:8557/h264',
    'Videolarm': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/mpeg4/1/media.amp',
    'VisionDigi': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'Visionite': f'rtsp://{username}:{password}@{IP}:{rtsp_port}',
    'VISTA': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/cam1/h264',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/'
        ],
    'VITEK': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/ch0.sdp',
    'Vivotek': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/live.sdp',
    'Weldex': f'rtsp://{username}:{password}@{IP}:7070/h264',
    'XM': f'rtsp://{IP}:{rtsp_port}/user={username}&{password}=&channel=1&stream=0.sdp?',
    'Y-cam': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/live_mpeg4.sdp',
    'Yudor': f'rtsp://{username}:{password}@{IP}:{rtsp_port}/',
    'Zavio': [
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/video.3gp',
        f'rtsp://{username}:{password}@{IP}:{rtsp_port}/video.mp4'
        ]
    }
    return rtsp_dict[camera_name]
