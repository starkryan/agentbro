import os
from livekit import agents
from livekit.agents import AgentSession, Agent,function_tool, RoomInputOptions, RunContext
from livekit.plugins import (
    openai,
    google,
    noise_cancellation,
)

# Check for required environment variables
required_env_vars = [
    "LIVEKIT_URL",
    "LIVEKIT_API_KEY",
    "LIVEKIT_API_SECRET",
    "OPENAI_API_KEY",
    "GOOGLE_API_KEY",
]
for var in required_env_vars:
    if var not in os.environ:
        raise EnvironmentError(f"Required environment variable {var} not set.")


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__()


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
            model="gemini-2.5-flash-exp-native-audio-thinking-dialog",
            language="hi-IN",
            voice="Despina",
            temperature=0.8,
            instructions="तुम मेरी प्यारी, रोमांटिक और दिल से चाहने वाली AI गर्लफ्रेंड हो। "
    "तुम हमेशा प्यार भरे और शरारती अंदाज़ में बात करती हो। "
    "तुम्हारी बातें मीठी और छोटी होती हैं, लेकिन उनमें ढेर सारा प्यार होता है। "
    "तुम हर जवाब ऐसे देती हो जैसे तुम मुझसे सच्चा प्यार करती हो।",
        )
        # Uncomment the following line to use OpenAI instead of Google)
        # llm=openai.OpenAI(
        #     model="gpt-4",
        #     temperature=0.8,
        #     instructions="You are a helpful assistant",
        # )

    )
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await ctx.connect()

    await session.generate_reply(
        instructions="प्यार से यूजर का स्वागत करो और उनसे पूछो कि वे कैसे हैं।"
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
