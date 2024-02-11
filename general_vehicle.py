
class Request(Model):
    message:str

@agent.on_interval(period=5.0)

async def send(ctx: Context):
    coordinate = ctx.storage.get("count") or 2000
    ctx.logger.info(f"My count is: {coordinate}")
    await ctx.send('agent1qta8q8vvtchuemuasx7x9dxluqvtn33hjj0s7s46sex5mzmrdzx6j8vn9sp', Request(message=coordinate))
    ctx.storage.set("count" , coordinate + 100)

@agent.on_message(model=Request)
async def handle_message(ctx: Context, sender: str, msg: Request):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")    
    
