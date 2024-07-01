from nada_dsl import *

def nada_main():
    # Define magical creatures as parties
    unicorn = Party(name="Unicorn")
    dragon = Party(name="Dragon")
    phoenix = Party(name="Phoenix")
    mermaid = Party(name="Mermaid")
    griffin = Party(name="Griffin")

    vote_unicorn = SecretInteger(Input(name="vote_unicorn_move", party=unicorn))
    vote_dragon = SecretInteger(Input(name="vote_dragon_move", party=dragon))
    vote_phoenix = SecretInteger(Input(name="vote_phoenix_move", party=phoenix))
    vote_mermaid = SecretInteger(Input(name="vote_mermaid_move", party=mermaid))
    vote_griffin = SecretInteger(Input(name="vote_griffin_move", party=griffin))

    magic_blast_votes = (vote_unicorn == 1) + (vote_dragon == 1) + (vote_phoenix == 1) + (vote_mermaid == 1) + (vote_griffin == 1)
    fire_breath_votes = (vote_unicorn == 2) + (vote_dragon == 2) + (vote_phoenix == 2) + (vote_mermaid == 2) + (vote_griffin == 2)
    healing_light_votes = (vote_unicorn == 3) + (vote_dragon == 3) + (vote_phoenix == 3) + (vote_mermaid == 3) + (vote_griffin == 3)
    water_wave_votes = (vote_unicorn == 4) + (vote_dragon == 4) + (vote_phoenix == 4) + (vote_mermaid == 4) + (vote_griffin == 4)
    lightning_strike_votes = (vote_unicorn == 5) + (vote_dragon == 5) + (vote_phoenix == 5) + (vote_mermaid == 5) + (vote_griffin == 5)

    most_popular_move = (magic_blast_votes > fire_breath_votes) & (magic_blast_votes > healing_light_votes) & (magic_blast_votes > water_wave_votes) & (magic_blast_votes > lightning_strike_votes) * 1 + \
                        (fire_breath_votes > magic_blast_votes) & (fire_breath_votes > healing_light_votes) & (fire_breath_votes > water_wave_votes) & (fire_breath_votes > lightning_strike_votes) * 2 + \
                        (healing_light_votes > magic_blast_votes) & (healing_light_votes > fire_breath_votes) & (healing_light_votes > water_wave_votes) & (healing_light_votes > lightning_strike_votes) * 3 + \
                        (water_wave_votes > magic_blast_votes) & (water_wave_votes > fire_breath_votes) & (water_wave_votes > healing_light_votes) & (water_wave_votes > lightning_strike_votes) * 4 + \
                        (lightning_strike_votes > magic_blast_votes) & (lightning_strike_votes > fire_breath_votes) & (lightning_strike_votes > healing_light_votes) & (lightning_strike_votes > water_wave_votes) * 5

    output = Output(most_popular_move, "most_popular_battle_move", unicorn)

    return [output]
