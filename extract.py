"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    collection_of_neo = []
    with open(neo_csv_path, 'r') as infile:
        next(infile)
        for line in infile:
            data = line.split(',')
            neo = NearEarthObject(designation=data[3], name=data[4], diameter=data[15], hazardous=data[7])
            collection_of_neo.append(neo)
    return collection_of_neo


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    collection_of_ca = []
    with open(cad_json_path, 'r') as infile:
        dataset = json.load(infile)
        for data in dataset['data']:
            ca = CloseApproach(_designation=data[0], time=data[3], distance=data[4], velocity=data[8])
            collection_of_ca.append(ca)
    return collection_of_ca