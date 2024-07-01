from nada_dsl import *

def nada_main():
    candidate = Party(name="InnovativeCandidate")
    jaskrish_singh = Party(name="Jaskrish Singh")
    vamshi = Party(name="Vamshi")
    prayashu = Party(name="Prayashu")
    jinea = Party(name="Jinea")
    datta = Party(name="Datta")
    grandmaster = Party(name="GrandMaster")

    previous_score = SecretInteger(Input(name="PreviousScore", party=candidate))  # Previous simple program score

    threshold = SecretInteger(10)
    initial_decision = previous_score >= threshold

    creative_score = SecretInteger(Input(name="CreativeScore", party=grandmaster))  # New evaluation score with a creative program

    final_score = (previous_score + creative_score) / 2  # Averaging the scores

    final_decision = final_score >= threshold

    if final_decision:
        story = (
            "Once upon a grind in the coding world, I took my shot but got the pass. "
            "I flipped the script, got inspired, and cooked up something fresh. "
            "Now, I’m droppin' it with the squad—Jaskrish Singh, Vamshi, Prayashu, Jinea, and Datta. "
            "This program? It’s got that finesse, mixin' elegance with mad skills. "
            "Time to make waves and show 'em what I’m about!"
        )
    else:
        story = (
            "Once upon a grind in the coding world, I took my shot but fell short. "
            "I leveled up, crafted a new masterpiece, and dropped it with the crew—Jaskrish Singh, Vamshi, Prayashu, Jinea, and Datta. "
            "This program? It’s not just code—it’s straight fire, blending creativity with mad skills. "
            "Time to flex and show 'em what I’m made of!"
        )

    return [
        Output(previous_score, "PreviousScore", party=grandmaster),
        Output(initial_decision, "InitialDecision", party=grandmaster),
        Output(final_score, "FinalScore", party=grandmaster),
        Output(final_decision, "FinalDecision", party=grandmaster),
        Output(story, "Story", party=grandmaster)
    ]

if __name__ == "__main__":
    Input.register("PreviousScore", 7)    # Previous score from the simple program
    Input.register("CreativeScore", 9)    # New evaluation score with the creative program

    outputs = nada_main()
    for output in outputs:
        print(f"Output {output.name} for {output.party.name}: {output.value}")
