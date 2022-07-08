user1 = {'name': 'Sorna', 'valid': True } #changing 'valid' will either run or not run the message_friends function.
user2 = {'name': 'Serena', 'valid': False}


def authenticated(fn):
  def auth(*args, **kwargs):
      if args[0]['valid']:
        return fn(*args, **kwargs)
      else:
        return print('not authorized to message')
  return auth


@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
message_friends(user2)
