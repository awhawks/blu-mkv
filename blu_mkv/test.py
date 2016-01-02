from .ffprobe import AbstractFfprobeController
from .mkvmerge import AbstractMkvmergeController


class StubFfprobeController(AbstractFfprobeController):
    def get_default_bluray_playlist_number(self, disc_path):
        all_playlists = self.get_bluray_playlists(disc_path)
        return max(all_playlists, key=lambda i: all_playlists[i]['duration'])

    def get_bluray_playlists(self, disc_path):
        return {
            28: {'duration': '3599.000000', 'size': '16970468350'},
            29: {'duration': '3600.000000', 'size': '16970468352'},
            419: {'duration': '7200.000000', 'size': '33940936704'}}

    def get_all_bluray_playlist_streams(self, disc_path, playlid_id):
        return [
            {'index': 0, 'codec_type': 'video'},
            {'index': 1, 'codec_type': 'audio'},
            {'index': 2, 'codec_type': 'audio'},
            {'index': 3, 'codec_type': 'subtitle'},
            {'index': 4, 'codec_type': 'subtitle'},
            {'index': 5, 'codec_type': 'subtitle'}]

    def get_bluray_playlist_subtitles_with_frames_count(
            self, disc_path, playlist_id):
        return [
            {'index': 3, 'nb_read_frames': '999'},
            {'index': 4, 'nb_read_frames': '1000'},
            {'index': 5, 'nb_read_frames': '2000'}]


class StubMkvmergeController(AbstractMkvmergeController):
    def get_file_info(self, file_path):
        return {
            "tracks": [
                {
                    "codec": "MPEG-4p10/AVC/h.264",
                    "id": 0,
                    "properties": {
                        "pixel_dimensions": "1920x1080",
                        "ts_pid": 4113,
                    },
                    "type": "video",
                },
                {
                    "codec": "DTS-HD Master Audio",
                    "id": 1,
                    "properties": {
                        "audio_channels": 6,
                        "audio_sampling_frequency": 48000,
                        "language": "fre",
                        "ts_pid": 4352,
                    },
                    "type": "audio",
                },
                {
                    "codec": "DTS-HD Master Audio",
                    "id": 2,
                    "properties": {
                        "audio_channels": 6,
                        "audio_sampling_frequency": 48000,
                        "language": "chi",
                        "ts_pid": 4353,
                    },
                    "type": "audio",
                },
                {
                    "codec": "HDMV PGS",
                    "id": 3,
                    "properties": {
                        "language": "fre",
                        "text_subtitles": True,
                        "ts_pid": 4608,
                    },
                    "type": "subtitles",
                },
                {
                    "codec": "HDMV PGS",
                    "id": 4,
                    "properties": {
                        "language": "fre",
                        "text_subtitles": True,
                        "ts_pid": 4609,
                    },
                    "type": "subtitles",
                },
                {
                    "codec": "HDMV PGS",
                    "id": 5,
                    "properties": {
                        "language": "chi",
                        "text_subtitles": True,
                        "ts_pid": 4610,
                    },
                    "type": "subtitles",
                },
            ],
        }
