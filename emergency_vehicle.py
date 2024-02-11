import requests
class Request(Model):
    message: str

global coordinate ,co

@agent.on_interval(period=5.0)

async def send(ctx: Context):
    coordinate = ctx.storage.get("count") or 1000
    # await ctx.send('agent1qta8q8vvtchuemuasx7x9dxluqvtn33hjj0s7s46sex5mzmrdzx6j8vn9sp', Request(message=coordinate))
    ctx.logger.info(f"coordinate of emergency vehicle is: {coordinate}")
    ctx.storage.set("count" , coordinate + 200)    

# This decorator tells the agent how to handle messages that match the 'Request' type. It will execute everytime a message is received.
@agent.on_message(model=Request)
async def handle_message(ctx: Context, sender: str, msg: Request):
    ctx.logger.info(f"coordinates of general vehicle {sender} is: {msg.message}")
    countt = ctx.storage.get("count")
    ctx.logger.info(int(msg.message) - countt)
    if(int(msg.message) - countt<500):
        co = ctx.storage.get("c") or 0
        ctx.storage.set("c" , co)
        c= ctx.storage.get("c")
        if(c<1):
            response = requests.get("https://e4fe-182-79-215-75.ngrok-free.app/notify/+919897957694")
            ctx.storage.set("c",c+1)
        


    