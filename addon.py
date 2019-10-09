from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "http://revolutionaryleftradio.libsyn.com/rss"
url2 = "https://itsgoingdown.org/feed/podcast"
url3 = "http://frombelowpodcast.libsyn.com/rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/7/3/3/a/733a93637e62338d/RLR_Logo_CROPPED_.jpg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://channelzeronetwork.com/wp-content/uploads/2019/05/igdlogo.jpg"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://is4-ssl.mzstatic.com/image/thumb/Podcasts113/v4/fa/12/d7/fa12d7cb-632e-67a2-4d89-759fcf9d9dc0/mza_6154833031004670653.jpg/600x600bb.jpg"},
    ]
    return items
@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items
@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items
if __name__ == '__main__':
    plugin.run()
