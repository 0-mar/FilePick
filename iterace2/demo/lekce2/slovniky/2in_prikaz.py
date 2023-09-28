slovnik = {"resolution": "1920x1200", "shaders": True, "texture_quality": "high", "max_fps": 120}

if "resolution" in slovnik:     # stejne jako slovnik.keys()
    print("Klic resolution je ve slovniku")

if 120 in slovnik.values():
    print("Hodnota 120 je ve slovniku")
