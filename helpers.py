# -*- coding: utf8 -*-

import pandas


IRI = 'https://annotations.libcrowds.com/export/playbills-results/'


def get_tag(bodies):
    for body in bodies:
        if body['purpose'] == 'tagging':
            return body['value']


def get_transcription(bodies):
    for body in bodies:
        if body['purpose'] == 'describing':
            return body['value']


def get_its_transcriptions_df():
    df = pandas.read_json(IRI, orient='records')
    df = df[df['motivation'] == 'describing']
    df['tag'] = df['body'].apply(get_tag)
    df['transcription'] = df['body'].apply(get_transcription)
    return df
