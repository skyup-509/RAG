from langchain_openai import ChatOpenAI

def get_llm(api_key: str, model: str = "google/diffusiongemma-26b-a4b-it"):
    return ChatOpenAI(
        model=model,
        api_key=api_key,
        base_url="https://integrate.api.nvidia.com/v1",
        temperature=0,
        max_tokens=100,
        timeout=180,
        extra_body={
            "chat_template_kwargs": {
                "enable_thinking": False
            }
        }
    )
    print("LLM 선언 완료")