import discord
from discord.ext.commands import DefaultHelpCommand


class helpformatter(DefaultHelpCommand):
    def get_ending_note(self):
        return "Made by Sasori#2776\n\nWebsite > github.com/slumpted"
