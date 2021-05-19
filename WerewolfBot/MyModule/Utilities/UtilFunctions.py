def IsInt(val):
    try:
        int(val)
    except ValueError:
        return False
    else:
        return True

async def WaitforInteger(client):
    message = await client.wait_for("message")
    if(IsInt(int(message.content))):
        return int(message.content)

    return None
