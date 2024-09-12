def test_gpt_response():
    gpt = GPTProvider(api_key="test-key")
    response = gpt.generate_text("¿Cómo está el clima?")
    assert response is not None
