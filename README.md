# Orchestral Playlist Generator

## Overview

The **Orchestral Playlist Generator** is a Python application designed to curate classical and orchestral soundtrack playlists for ballet dancers and enthusiasts. Playlists are categorized based on emotional moods such as **Heroic**, **Lively**, **Sentimental**, and **Dark**. Originally built using the Spotify API, the project is now archived due to Spotify API restrictions as of 2025.

## Features

- Mood-based playlist generation.
- Selection of classical and orchestral tracks optimized for ballet dancing.
- Audio feature analysis for refining track suitability (historical functionality).

## Tech Stack

- **Programming Language**: Python 3.10+
- **Libraries**:
  - `requests`
  - `base64`
  - `random`
- **External API**:
  - Spotify Web API (Access revoked April 2025)

## Screenshots

### Successful Playlist Generation (Historical)
   ```bash
Six Etudes for Piano - q = 96 by Philip Glass
https://open.spotify.com/track/7bYwm4LQaOsardfDdbVZg6
{'album': {'album_type': 'COMPILATION', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0LyfQWJT6nXafLPZqxe9Of'}, 'href': 'https://api.spotify.com/v1/artists/0LyfQWJT6nXafLPZqxe9Of', 'id': '0LyfQWJT6nXafLPZqxe9Of', 'name': 'Various Artists', 'type': 'artist', 'uri': 'spotify:artist:0LyfQWJT6nXafLPZqxe9Of'}], 'available_markets': ['AR', 'AT', 'BE', 'BO', 'BR', 'BG', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK'], 'external_urls': {'spotify': 'https://open.spotify.com/album/5cbAqQZSEgRiiNjuEHWTXc'}, 'href': 'https://api.spotify.com/v1/albums/5cbAqQZSEgRiiNjuEHWTXc', 'id': '5cbAqQZSEgRiiNjuEHWTXc', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273e6e0891de00a924b0f186d0c', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02e6e0891de00a924b0f186d0c', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851e6e0891de00a924b0f186d0c', 'width': 64}], 'name': 'Moulin Rouge', 'release_date': '2001-09-03', 'release_date_precision': 'day', 'total_tracks': 16, 'type': 'album', 'uri': 'spotify:album:5cbAqQZSEgRiiNjuEHWTXc'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0ExYzTb7raTAfsXPtiI5vq'}, 'href': 'https://api.spotify.com/v1/artists/0ExYzTb7raTAfsXPtiI5vq', 'id': '0ExYzTb7raTAfsXPtiI5vq', 'name': 'Nicole Kidman', 'type': 'artist', 'uri': 'spotify:artist:0ExYzTb7raTAfsXPtiI5vq'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/105Paee9vmV5rfLSG652e1'}, 'href': 'https://api.spotify.com/v1/artists/105Paee9vmV5rfLSG652e1', 'id': '105Paee9vmV5rfLSG652e1', 'name': 'Ewan McGregor', 'type': 'artist', 'uri': 'spotify:artist:105Paee9vmV5rfLSG652e1'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/5R51XX6tR8R2zlBYRmXm0o'}, 'href': 'https://api.spotify.com/v1/artists/5R51XX6tR8R2zlBYRmXm0o', 'id': '5R51XX6tR8R2zlBYRmXm0o', 'name': 'Jamie Allen', 'type': 'artist', 'uri': 'spotify:artist:5R51XX6tR8R2zlBYRmXm0o'}], 'available_markets': ['AR', 'AT', 'BE', 'BO', 'BR', 'BG', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK'], 'disc_number': 1, 'duration_ms': 251560, 'explicit': False, 'external_ids': {'isrc': 'USIR10110328'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/6fyv22stUNmoay5lLS0hHE'}, 'href': 'https://api.spotify.com/v1/tracks/6fyv22stUNmoay5lLS0hHE', 'id': '6fyv22stUNmoay5lLS0hHE', 'is_local': False, 'name': 'Elephant Love Medley - From "Moulin Rouge" Soundtrack', 'popularity': 45, 'preview_url': None, 'track_number': 10, 'type': 'track', 'uri': 'spotify:track:6fyv22stUNmoay5lLS0hHE'}
Elephant Love Medley - From "Moulin Rouge" Soundtrack by Nicole Kidman
https://open.spotify.com/track/6fyv22stUNmoay5lLS0hHE
{'album': {'album_type': 'ALBUM', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0YC192cP3KPCRWx8zr8MfZ'}, 'href': 'https://api.spotify.com/v1/artists/0YC192cP3KPCRWx8zr8MfZ', 'id': '0YC192cP3KPCRWx8zr8MfZ', 'name': 'Hans Zimmer', 'type': 'artist', 'uri': 'spotify:artist:0YC192cP3KPCRWx8zr8MfZ'}], 'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'PR', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK'], 'external_urls': {'spotify': 'https://open.spotify.com/album/2qvA7HmSg1iM6XMiFF76dp'}, 'href': 'https://api.spotify.com/v1/albums/2qvA7HmSg1iM6XMiFF76dp', 'id': '2qvA7HmSg1iM6XMiFF76dp', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273a883e26f90ab617c91b90e56', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02a883e26f90ab617c91b90e56', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851a883e26f90ab617c91b90e56', 'width': 64}], 'name': 'Inception (Music from the Motion Picture)', 'release_date': '2010-07-09', 'release_date_precision': 'day', 'total_tracks': 12, 'type': 'album', 'uri': 'spotify:album:2qvA7HmSg1iM6XMiFF76dp'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0YC192cP3KPCRWx8zr8MfZ'}, 'href': 'https://api.spotify.com/v1/artists/0YC192cP3KPCRWx8zr8MfZ', 'id': '0YC192cP3KPCRWx8zr8MfZ', 'name': 'Hans Zimmer', 'type': 'artist', 'uri': 'spotify:artist:0YC192cP3KPCRWx8zr8MfZ'}], 'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'PR', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK'], 'disc_number': 1, 'duration_ms': 570260, 'explicit': False, 'external_ids': {'isrc': 'USRE11000575'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/3iR6S8t0mOLUZUAB77KgrP'}, 'href': 'https://api.spotify.com/v1/tracks/3iR6S8t0mOLUZUAB77KgrP', 'id': '3iR6S8t0mOLUZUAB77KgrP', 'is_local': False, 'name': 'Waiting for a Train', 'popularity': 36, 'preview_url': 'https://p.scdn.co/mp3-preview/dc65304386566e73cb8540db931aa4be3f414f09?cid=ad0a8a8060204743b49d7c939c75563b', 'track_number': 10, 'type': 'track', 'uri': 'spotify:track:3iR6S8t0mOLUZUAB77KgrP'}
Waiting for a Train by Hans Zimmer
https://open.spotify.com/track/3iR6S8t0mOLUZUAB77KgrP
{'album': {'album_type': 'ALBUM', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6ihTqrjBvMSgztCI4BTQCY'}, 'href': 'https://api.spotify.com/v1/artists/6ihTqrjBvMSgztCI4BTQCY', 'id': '6ihTqrjBvMSgztCI4BTQCY', 'name': 'Elite Force', 'type': 'artist', 'uri': 'spotify:artist:6ihTqrjBvMSgztCI4BTQCY'}], 'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'PR', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK'], 'external_urls': {'spotify': 'https://open.spotify.com/album/4860OEeDMm3oXgKMzTZnrM'}, 'href': 'https://api.spotify.com/v1/albums/4860OEeDMm3oXgKMzTZnrM', 'id': '4860OEeDMm3oXgKMzTZnrM', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273ac698a0ac33115bd22dbdc14', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02ac698a0ac33115bd22dbdc14', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851ac698a0ac33115bd22dbdc14', 'width': 64}], 'name': 'Nipped & Tucked (Volume One)', 'release_date': '2024-03-14', 'release_date_precision': 'day', 'total_tracks': 10, 'type': 'album', 'uri': 'spotify:album:4860OEeDMm3oXgKMzTZnrM'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6ihTqrjBvMSgztCI4BTQCY'}, 'href': 'https://api.spotify.com/v1/artists/6ihTqrjBvMSgztCI4BTQCY', 'id': '6ihTqrjBvMSgztCI4BTQCY', 'name': 'Elite Force', 'type': 'artist', 'uri': 'spotify:artist:6ihTqrjBvMSgztCI4BTQCY'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/03GruNQP8X25PCoWzdvIGZ'}, 'href': 'https://api.spotify.com/v1/artists/03GruNQP8X25PCoWzdvIGZ', 'id': '03GruNQP8X25PCoWzdvIGZ', 'name': 'Klaus Badelt', 'type': 'artist', 'uri': 'spotify:artist:03GruNQP8X25PCoWzdvIGZ'}], 'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'PR', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK'], 'disc_number': 1, 'duration_ms': 185581, 'explicit': False, 'external_ids': {'isrc': 'QZES72401419'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/6VQ5YrFgPY5iG0cSFmjf2P'}, 'href': 'https://api.spotify.com/v1/tracks/6VQ5YrFgPY5iG0cSFmjf2P', 'id': '6VQ5YrFgPY5iG0cSFmjf2P', 'is_local': False, 'name': 'Brknck - Nipped & Tucked', 'popularity': 6, 'preview_url': 'https://p.scdn.co/mp3-preview/b948608113d761fcc1006fda72843fde1df164ad?cid=ad0a8a8060204743b49d7c939c75563b', 'track_number': 6, 'type': 'track', 'uri': 'spotify:track:6VQ5YrFgPY5iG0cSFmjf2P'}
   ```

### Current API Error (Post Spotify Changes)


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/deberry-code/orchestral-playlist-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd orchestral-playlist-generator
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

> Note: Due to Spotify API restrictions, this project is currently non-functional.

1. Update your Spotify `client_id` and `client_secret` in the Python script.
2. Run the script:
   ```bash
   python playlist_generator.py
   ```
3. Select a mood (heroic, lively, sentimental, dark) to generate a playlist.

## Future Improvements (If API Access Restored)

- Integrate other music platforms (Deezer, Apple Music, YouTube Music).
- Local dataset creation using public domain classical music.
- User-friendly GUI for easier interaction.
- Offline playlist caching.

