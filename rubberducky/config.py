import os
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.ERROR)


logger.info("In config file")

config = {

    'OFFENSIVE_WORDS': [
        "skank",
        "ass",
        "wetback",
        "bitch",
        "blow job",
        "blowjob",
        "cunt",
        "dick",
        "douchebag",
        "dyke",
        "fag",
        "nigger",
        "tranny",
        "trannies",
        "paki",
        "pussy",
        "retard",
        "slut",
        "titt",
        "tits",
        "poop",
        "pee"
        "wop",
        "whore",
        "chink",
        "fatass",
        "shemale",
        "shit",
        "shithole",
        "nigga",
        "daygo",
        "dego",
        "dago",
        "gook",
        "kike",
        "kraut",
        "spic",
        "twat",
        "lesbo",
        "homo",
        "fatso",
        "lardass",
        "jap",
        "biatch",
        "tard",
        "gimp",
        "gyp",
        "chinaman",
        "chinamen",
        "golliwog",
        "crip",
        "raghead",
        "negro",
        "hooker",
        "damn",
        "god damn",
        "goddamn",
        "fuck",
        "test1234",
        "loser",
        "murder",
        "slaughter",
        "kill",
        "asshole"
        ],

    'DANGER_WORDS': [
        "suicidal",
        "suicide",
        "abortion",
        "pregnant",
        "miscarry",
        "miscarriage",
        "abuse",
        "abusive",
        "self-harm",
        "anorexia",
        "bulemia"
        "mental illness",
        "assault",
        "rape",
        "sexual assault",
        "dangertest",
        "unsafe"
        ],

}

