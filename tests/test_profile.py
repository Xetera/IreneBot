from unittest.mock import Mock
import pytest
import discord
from discord.ext import commands



msg_data = {
'id': '1',
'webhook_id': '1',
'attachments': [],
'embeds': [],
'edited_timestamp': None,
'type': None,
'pinned': None,
'mention_everyone': False,
'tts': False,
'content': "test",
'nonce': None,
'message_reference': None
}


msg_mock = Mock(discord.Message(state=None, channel=None, data=msg_data))

prefix_arg = {'message': msg_mock, 'prefix': '%'}
ctx_mock = Mock(commands.Context(**prefix_arg))
# print(ctx_mock)

@pytest.fixture
def ctx():


    return



def check_user(ctx):
    pass



