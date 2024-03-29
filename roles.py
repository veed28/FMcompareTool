from attributes import corners, crossing, free_kicks, heading, dribbling, long_shots, long_throws, marking, penalty_taking, tackling, aggression, bravery, concentration, determination, leadership, positioning, teamwork, work_rate, jumping_reach, natural_fitness, stamina, pace, strength, composure, decisions, flair, off_the_ball, vision, acceleration, agility, balance, anticipation, finishing, first_touch, passing, technique

class Role:

    def __init__(self, player, final_list):
        self.player = final_list[37 * player]
        self.dribbling = 1.2 * dribbling(player, final_list)
        self.finishing = finishing(player, final_list)
        self.first_touch = first_touch(player, final_list)
        self.passing = passing(player, final_list)
        self.technique = technique(player, final_list)
        self.anticipation = 1.2 * anticipation(player, final_list)
        self.composure = composure(player, final_list)
        self.decisions = decisions(player, final_list)
        self.flair = flair(player, final_list)
        self.off_the_ball = off_the_ball(player, final_list)
        self.vision = vision(player, final_list)
        self.acceleration = 1.2 * acceleration(player, final_list)
        self.agility = 1.2 * agility(player, final_list)
        self.balance = 1.2 * balance(player, final_list)
        self.concentration = 1.2 * concentration(player, final_list)
        self.work_rate = work_rate(player, final_list)
        self.pace = 1.2 * pace(player, final_list)
        self.stamina = 1.2 * stamina(player, final_list)
        self.long_shots = long_shots(player, final_list)
        self.teamwork = teamwork(player, final_list)
        self.strength = 1.2 * strength(player, final_list)
        self.marking = marking(player, final_list)
        self.tackling = tackling(player, final_list)
        self.positioning = positioning(player, final_list)
        self.crossing = crossing(player, final_list)
        self.aggression = aggression(player, final_list)
        self.bravery = bravery(player, final_list)
        self.heading = heading(player, final_list)
        self.jumping_reach = jumping_reach(player, final_list)
        self.long_throws = 0.2 * long_throws(player, final_list)
        self.corners = 0.4 * corners(player, final_list)
        self.free_kicks = 0.4 * free_kicks(player, final_list)
        self.penalty_taking = 0.4 * penalty_taking(player, final_list)

    def complete_wing_back_s(self):
        self.score = (self.crossing * 2) + (self.dribbling * 2) + self.first_touch + self.marking + self.passing + self.tackling + (self.technique * 2) + self.anticipation + self.decisions + self.flair + (self.off_the_ball * 2) + self.positioning + (self.teamwork * 2) + (self.work_rate * 2) + (self.acceleration * 2) + self.agility + self.balance + self.pace + (self.stamina * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def complete_wing_back_a(self):
        self.score = (self.crossing * 2) + (self.dribbling * 2) + self.first_touch + self.marking + self.passing + self.tackling + (self.technique * 2) + self.anticipation + self.decisions + (self.flair * 2) + (self.off_the_ball * 2) + self.positioning + (self.teamwork * 2) + (self.work_rate * 2) + (self.acceleration * 2) + self.agility + self.balance + self.pace + (self.stamina * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def inverted_wing_back_s(self):
        self.score = (self.first_touch * 2) + self.marking + (self.passing * 2) + (self.tackling * 2) + self.technique + self.anticipation + (self.composure * 2) + self.concentration + (self.decisions * 2) + self.off_the_ball + self.positioning + (self.teamwork * 2) + self.vision + self.work_rate + self.acceleration + self.agility + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def inverted_wing_back_d(self):
        self.score = self.first_touch + self.marking + (self.passing * 2) + (self.tackling * 2) + self.technique + (self.anticipation * 2) + self.composure + self.concentration + (self.decisions * 2) + self.off_the_ball + (self.positioning * 2) + (self.teamwork * 2) + self.work_rate + self.acceleration + self.agility + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def inverted_wing_back_a(self):
        self.score = self.crossing + self.dribbling + (self.first_touch * 2) + self.long_shots + self.marking + (self.passing * 2) + (self.tackling * 2) + (self.technique * 2) + self.anticipation + (self.composure * 2) + self.concentration + (self.decisions * 2) + (self.off_the_ball * 2) + self.positioning + (self.teamwork * 2) + (self.vision * 2) + self.work_rate + (self.acceleration * 2) + self.agility + self.pace + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def inverted_full_back(self):
        self.score = self.dribbling + self.first_touch + (self.heading * 2) + (self.marking * 2) + self.passing + (self.tackling * 2) + self.technique + self.aggression + self.anticipation + self.bravery + self.composure + self.concentration + self.decisions + (self.positioning * 2) + self.work_rate + self.agility + self.jumping_reach + self.pace + (self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def wing_back_s(self):
        self.score = (self.crossing * 2) + (self.dribbling * 2) + self.first_touch + (self.marking * 2) + self.passing + (self.tackling * 2) + self.technique + self.anticipation + self.concentration + self.decisions + (self.off_the_ball * 2) + self.positioning + (self.teamwork * 2) + (self.work_rate * 2) + (self.acceleration * 2) + self.agility + self.balance + self.pace + (self.stamina * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def wing_back_d(self):
        self.score = self.crossing + self.dribbling + self.first_touch + (self.marking * 2) + self.passing + (self.tackling * 2) + self.technique + (self.anticipation * 2) + self.concentration + self.decisions + self.off_the_ball + (self.positioning * 2) + (self.teamwork * 2) + (self.work_rate * 2) + (self.acceleration * 2) + self.agility + self.balance + self.pace + (self.stamina * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def wing_back_a(self):
        self.score = (self.crossing * 2) + (self.dribbling * 2) + self.first_touch + self.marking + self.passing + (self.tackling * 2) + (self.technique * 2) + self.anticipation + self.concentration + self.decisions + self.flair + (self.off_the_ball * 2) + self.positioning + (self.teamwork * 2) + (self.work_rate * 2) + (self.acceleration * 2) + self.agility + self.balance + (self.pace * 2) + (self.stamina * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def central_defender_d(self):
        self.score = (self.heading * 2) + (self.marking * 2) + (
                    self.tackling * 2) + self.aggression + self.anticipation + self.bravery +self.composure + self.concentration + self.decisions + (
                                 self.positioning * 2) + (self.jumping_reach * 2) + self.pace + (
                                 self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def central_defender_s(self):
        self.score = (self.heading * 2) + self.marking + (
                    self.tackling * 2) + (self.aggression * 2) + self.anticipation + (self.bravery * 2) + self.composure + self.concentration + (self.decisions * 2) + (
                                 self.positioning * 2) + (self.jumping_reach * 2) + (self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def central_defender_c(self):
        self.score = self.heading + (self.marking * 2) + (
                    self.tackling * 2) + (self.anticipation * 2) + self.bravery + self.composure + (self.concentration * 2) + (self.decisions * 2) + (
                                 self.positioning * 2) + self.jumping_reach + (self.pace * 2) + self.strength + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def ball_playing_defender_d(self):
        self.score = self.first_touch + (self.heading * 2) + (self.marking * 2) + (self.passing * 2) + (
                    self.tackling * 2) + self.technique + self.aggression + self.anticipation + self.bravery + (
                                 self.composure * 2) + self.concentration + self.decisions + (
                                 self.positioning * 2) + self.vision + (self.jumping_reach * 2) + self.pace + (
                                 self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def ball_playing_defender_s(self):
        self.score = self.first_touch + (self.heading * 2) + self.marking + (self.passing * 2) + (
                    self.tackling * 2) + self.technique + (self.aggression * 2) + self.anticipation + (
                                 self.bravery * 2) + (self.composure * 2) + self.concentration + (
                                 self.decisions * 2) + (self.positioning * 2) + self.vision + (
                                 self.jumping_reach * 2) + (self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def ball_playing_defender_c(self):
        self.score = self.first_touch + self.heading + (self.marking * 2) + (self.passing * 2) + (
                    self.tackling * 2) + self.technique + (self.anticipation * 2) + self.bravery + (
                                 self.composure * 2) + (self.concentration * 2) + (self.decisions * 2) + (
                                 self.positioning * 2) + self.vision + self.jumping_reach + (
                                 self.pace * 2) + self.strength + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def wide_center_back_d(self):
        self.score = self.dribbling + self.first_touch + (self.heading * 2) + (self.marking * 2) + self.passing + (
                    self.tackling * 2) + self.technique + self.anticipation + self.bravery + self.composure + self.concentration + self.decisions + (
                                 self.positioning * 2) + self.work_rate + self.agility + (
                                 self.jumping_reach * 2) + self.pace + (self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def wide_center_back_s(self):
        self.score = self.crossing + (self.dribbling * 2) + self.first_touch + (self.heading * 2) + (self.marking * 2) + self.passing + (
                    self.tackling * 2) + self.technique + self.anticipation + self.bravery + self.composure + self.concentration + self.decisions + self.off_the_ball + (
                                 self.positioning * 2) + self.work_rate + self.agility + (
                                 self.jumping_reach * 2) + (self.pace * 2) + self.stamina + (self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def wide_center_back_a(self):
        self.score = (self.crossing * 2) + (self.dribbling * 2) + self.first_touch + (self.heading * 2) + (
                    self.marking * 2) + self.passing + (
                             self.tackling * 2) + self.technique + self.anticipation + self.bravery + self.composure + self.concentration + self.decisions + (self.off_the_ball * 2) + self.positioning + self.work_rate + self.agility + (
                             self.jumping_reach * 2) + (self.pace * 2) + (self.stamina * 2) + (self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def libero_d(self):
        self.score = (self.first_touch * 2) + (self.heading * 2) + (
                    self.marking * 2) + self.passing + (
                             self.tackling * 2) + (self.technique * 2) + self.anticipation + self.bravery + (self.composure * 2) + self.concentration + (self.decisions * 2) + (self.positioning * 2) + (self.teamwork * 2) + (
                             self.jumping_reach * 2) + self.pace + self.stamina + (self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def libero_s(self):
        self.score = self.dribbling + (self.first_touch * 2) + (self.heading * 2) + (
                    self.marking * 2) + (self.passing * 2) + (
                             self.tackling * 2) + (self.technique * 2) + self.anticipation + self.bravery + (self.composure * 2) + self.concentration + (self.decisions * 2) + (self.positioning * 2) + (self.teamwork * 2) + self.vision +(
                             self.jumping_reach * 2) + self.pace + self.stamina + (self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def ball_winning_midfielder_d(self):
        self.score = self.marking + (
                    self.tackling * 2) + (self.aggression * 2) + (self.anticipation * 2) + self.bravery + self.concentration + self.positioning + (self.teamwork * 2) + (self.work_rate * 2) + self.agility + self.pace + (self.stamina * 2) + (
                                 self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def ball_winning_midfielder_s(self):
        self.score = self.marking + self.passing + (
                    self.tackling * 2) + (self.aggression * 2) + (self.anticipation * 2) + self.bravery + self.concentration + (self.teamwork * 2) + (self.work_rate * 2) + self.agility + self.pace + (self.stamina * 2) + (
                                 self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def defensive_midfielder_d(self):
        self.score = self.marking + self.passing + (
                    self.tackling * 2) + self.aggression + (self.anticipation * 2) + self.composure + (self.concentration * 2) + self.decisions + (self.positioning * 2) + (self.teamwork * 2) + self.work_rate + self.stamina + self.strength + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score
    def defensive_midfielder_s(self):
        self.score = self.first_touch + self.marking + self.passing + (
                    self.tackling * 2) + self.aggression + (self.anticipation * 2) + self.composure + (self.concentration * 2) + self.decisions + (self.positioning * 2) + (self.teamwork * 2) + self.work_rate + self.stamina + self.strength + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def segundo_volante_s(self):
        self.score = self.finishing + self.first_touch + self.long_shots + (self.marking * 2) + (self.passing * 2) + (
                    self.tackling * 2) + self.anticipation + self.composure + self.concentration + self.decisions + (self.off_the_ball) + (
                self.positioning * 2) + (self.work_rate * 2) + self.acceleration + self.balance + (self.pace * 2) + (self.stamina * 2) + self.strength + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def segundo_volante_a(self):
        self.score = (self.finishing * 2) + self.first_touch + (self.long_shots * 2) + self.marking + (self.passing * 2) + (
                    self.tackling * 2) + (self.anticipation * 2) + self.composure + self.concentration + self.decisions + (self.off_the_ball) + (
                self.positioning * 2) + (self.work_rate * 2) + self.acceleration + self.balance + (self.pace * 2) + (self.stamina * 2) + self.strength + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def half_back(self):
        self.score = self.first_touch + (self.marking * 2) + self.passing + (
                    self.tackling * 2) + self.aggression + (self.anticipation * 2) + self.bravery + (self.composure * 2) + (self.concentration * 2) + (self.decisions * 2) + (
                                 self.positioning * 2) + (self.teamwork * 2) + self.work_rate + self.jumping_reach + self.stamina + self.strength + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def anchor(self):
        self.score = (self.marking * 2) +(self.tackling * 2) + (self.anticipation * 2) + self.composure + (self.concentration * 2) + (self.decisions * 2) + (
                                 self.positioning * 2) + self.teamwork + self.strength + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def deep_lying_playmaker_d(self):
        self.score = (self.first_touch * 2) + (self.passing * 2) + self.tackling + (
                    self.technique * 2) + self.anticipation + (self.composure * 2) + (
                                 self.decisions * 2) + self.positioning + (self.teamwork * 2) + (
                                 self.vision * 2) + self.balance + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def deep_lying_playmaker_s(self):
        self.score = (self.first_touch * 2) + (self.passing * 2) + (
                    self.technique * 2) + self.anticipation + (self.composure * 2) + (
                                 self.decisions * 2) + self.off_the_ball + self.positioning + (self.teamwork * 2) + (
                                 self.vision * 2) + self.balance + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def roaming_playmaker(self):
        self.score = self.dribbling + (self.first_touch * 2) + self.long_shots + (self.passing * 2) + (
                    self.technique * 2) + (self.anticipation * 2) + (self.composure * 2) + self.concentration + (
                                 self.decisions * 2) + (self.off_the_ball * 2) + self.positioning + (self.teamwork * 2) + (
                                 self.vision * 2) + (self.work_rate * 2) + (self.acceleration * 2) + self.agility + self.balance + self.pace + (self.stamina * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def regista(self):
        self.score = self.dribbling + (self.first_touch * 2) + self.long_shots + (self.passing * 2) + (
                    self.technique * 2) + self.anticipation + (self.composure * 2) + (
                                 self.decisions * 2) + (self.flair * 2) + (self.off_the_ball * 2) + (self.teamwork * 2) + (
                                 self.vision * 2) + self.balance + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def mezzala_s(self):
        self.score = self.dribbling + self.first_touch + self.long_shots + (self.passing * 2) + self.tackling + (
                    self.technique * 2) + self.anticipation + self.composure + (self.decisions * 2) + (
                self.off_the_ball * 2) + self.vision + (self.work_rate * 2) + (self.acceleration * 2) + self.balance + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def mezzala_a(self):
        self.score = (self.dribbling * 2) + self.finishing + self.first_touch + self.long_shots + (self.passing * 2) + (
                    self.technique * 2) + self.anticipation + self.composure + (self.decisions * 2) + self.flair + (
                self.off_the_ball * 2) + (self.vision * 2) + (self.work_rate * 2) + (self.acceleration * 2) + self.balance + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def central_midfielder_d(self):
        self.score = self.first_touch + self.marking + self.passing + (
                    self.tackling * 2) + self.technique + self.aggression + self.anticipation + self.composure + (
                                 self.concentration * 2) + (self.decisions * 2) + (self.positioning * 2) + (
                                 self.teamwork * 2) + self.work_rate + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def central_midfielder_s(self):
        self.score = (self.first_touch * 2) + (self.passing * 2) + (
                    self.tackling * 2) + self.technique + self.anticipation + self.composure + self.concentration + (self.decisions * 2) + self.off_the_ball + (
                                 self.teamwork * 2) + self.vision + self.work_rate + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def central_midfielder_a(self):
        self.score = (self.first_touch * 2) + self.long_shots + (self.passing * 2) + self.tackling + self.technique + self.anticipation + self.composure + (self.decisions * 2) + (self.off_the_ball * 2) + self.teamwork + self.vision + self.work_rate + self.acceleration + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score


    def box_to_box_midfielder(self):
        self.score = self.dribbling + self.finishing + self.first_touch + self.long_shots + (self.passing * 2) + (self.tackling * 2) + self.technique + self.aggression + self.anticipation + self.composure + self.decisions + (self.off_the_ball * 2) + self.positioning + (self.teamwork * 2) + (
                                 self.work_rate * 2) + self.acceleration + self.balance + self.pace + (self.stamina) + self.strength + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def carrilero(self):
        self.score = (self.first_touch * 2) + (self.passing * 2) + (self.tackling) + self.technique + self.anticipation + self.composure + self.concentration + (
                                 self.decisions * 2) + self.off_the_ball + (self.positioning * 2) + (self.teamwork * 2) + self.vision + self.work_rate + (self.stamina * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def winger_s(self):
        self.score = (self.crossing * 2) + (self.dribbling * 2) + self.first_touch + self.passing + (self.technique * 2) + self.off_the_ball * 2 + self.work_rate * 2 + (self.acceleration * 2) + (self.agility * 2) + self.balance + self.pace + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def winger_a(self):
        self.score = (self.crossing * 2) + (self.dribbling * 2) + self.first_touch + self.passing + (self.technique * 2) + self.anticipation + self.flair + self.off_the_ball * 2 + self.work_rate * 2 + (self.acceleration * 2) + (self.agility * 2) + self.balance + self.pace + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def inverted_winger_s(self):
        self.score = (self.crossing * 2) + (self.dribbling * 2) + self.first_touch + self.long_shots + (self.passing * 2) + (self.technique * 2) + self.composure + self.decisions + self.off_the_ball + self.vision + self.work_rate + (self.acceleration * 2) + (self.agility * 2) + self.balance + self.pace + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def inverted_winger_a(self):
        self.score = (self.crossing * 2) + (self.dribbling * 2) + self.first_touch + self.long_shots + (self.passing * 2) + (self.technique * 2) + self.composure + self.decisions + self.flair + self.off_the_ball + self.vision + self.work_rate + (self.acceleration * 2) + (self.agility * 2) + self.balance + self.pace + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def inside_forward_s(self):
        self.score = (self.dribbling * 2) + (self.finishing * 2) + (self.first_touch * 2) + self.long_shots + (self.passing * 2) + (self.technique * 2) + self.anticipation + self.composure + (self.off_the_ball * 2) + self.vision + self.work_rate + (self.acceleration * 2) + (self.agility * 2) + self.balance + self.pace + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def inside_forward_a(self):
        self.score = (self.dribbling * 2) + (self.finishing * 2) + (self.first_touch * 2) + self.long_shots + (self.passing * 2) + (self.technique * 2) + (self.anticipation * 2) + self.composure + (self.off_the_ball * 2) + self.work_rate + (self.acceleration * 2) + (self.agility * 2) + self.balance + self.pace + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def raumdeuter(self):
        self.score = (self.finishing * 2) + self.first_touch + self.technique + (self.anticipation * 2) + (self.composure * 2) + (self.concentration * 2) + (self.decisions * 2) + (self.off_the_ball * 2) + self.work_rate + self.acceleration + (self.balance * 2) + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def wide_target_forward_s(self):
        self.score = self.crossing + self.first_touch + self.heading + self.anticipation + (self.bravery * 2) + self.off_the_ball + self.positioning + (self.teamwork * 2) + self.work_rate + self.balance + (self.jumping_reach * 2) + self.stamina + (self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def wide_target_forward_a(self):
        self.score = self.crossing + self.finishing + self.first_touch + self.heading + self.anticipation + (self.bravery * 2) + self.off_the_ball + self.positioning + (self.teamwork * 2) + self.work_rate + self.balance + (self.jumping_reach * 2) + self.stamina + (self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def wide_playmaker_s(self):
        self.score = self.dribbling + (self.first_touch * 2) + (self.passing * 2) + (
                    self.technique * 2) + (self.composure * 2) + (
                                 self.decisions * 2) + self.off_the_ball + (self.teamwork * 2) + (
                                 self.vision * 2) + self.agility + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def wide_playmaker_a(self):
        self.score = (self.dribbling * 2) + (self.first_touch * 2) + (self.passing * 2) + (
                    self.technique * 2) + self.anticipation + (self.composure * 2) + (
                                 self.decisions * 2) + self.flair + (self.off_the_ball * 2) + (self.teamwork * 2) + (
                                 self.vision * 2) + self.acceleration + self.agility + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def defensive_winger_d(self):
        self.score = self.crossing + self.dribbling + self.first_touch + self.marking + self.tackling + (self.technique * 2) + self.aggression + self.anticipation + self.concentration + self.decisions + (self.off_the_ball * 2) + (self.positioning * 2) + (self.teamwork * 2) + (self.work_rate * 2) + self.acceleration + (self.stamina * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def defensive_winger_s(self):
        self.score = (self.crossing * 2) + self.dribbling + self.first_touch + self.marking + self.passing + self.tackling + (self.technique * 2) + self.aggression + self.anticipation + self.composure + self.concentration + self.decisions + (self.off_the_ball * 2) + self.positioning + (self.teamwork * 2) + (self.work_rate * 2) + self.acceleration + (self.stamina * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def wide_midfielder_d(self):
        self.score = self.crossing + self.first_touch + self.marking + (self.passing * 2) + (self.tackling * 2) + self.technique + self.anticipation + self.composure + (self.concentration * 2) + (self.decisions * 2) + (self.positioning * 2) + (self.work_rate * 2) + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def wide_midfielder_s(self):
        self.score = self.crossing + self.first_touch + (self.passing * 2) + (self.tackling * 2) + self.technique + self.anticipation + self.composure + self.concentration + (self.decisions * 2) + self.off_the_ball + self.positioning + (self.teamwork * 2) + self.vision + (self.work_rate * 2) + (self.stamina * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def wide_midfielder_a(self):
        self.score = (self.crossing * 2) + (self.first_touch * 2) + (self.passing * 2) + self.tackling + self.technique + self.anticipation + self.composure + (self.decisions * 2) + self.off_the_ball + (self.teamwork * 2) + self.vision + (self.work_rate * 2) + (self.stamina * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def trequartista(self):
        self.score = (self.dribbling * 2) + self.finishing + (self.first_touch * 2) + (self.passing * 2) + (
                    self.technique * 2) + self.anticipation + (self.composure * 2) + (self.decisions * 2) + (
                                 self.flair * 2) + (self.off_the_ball * 2) + (self.vision * 2) + (
                                 self.acceleration * 2) + self.agility + self.balance + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def attacking_midfielder_s(self):
        self.score = self.dribbling + (self.first_touch * 2) + (self.long_shots * 2) + (self.passing * 2) + (
                    self.technique * 2) + (self.anticipation * 2) + self.composure + (self.decisions * 2) + (
                                 self.flair * 2) + (self.off_the_ball * 2) + self.vision + self.agility + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def advanced_playmaker_s(self):
        self.score = self.dribbling + (self.first_touch * 2) + (self.passing * 2) + (
                    self.technique * 2) + self.anticipation + (self.composure * 2) + (
                                 self.decisions * 2) + self.flair + (self.off_the_ball * 2) + (self.teamwork * 2) + (
                                 self.vision * 2) + self.agility + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def advanced_playmaker_a(self):
        self.score = self.dribbling + (self.first_touch * 2) + (self.passing * 2) + (
                    self.technique * 2) + self.anticipation + (self.composure * 2) + (
                                 self.decisions * 2) + self.flair + (self.off_the_ball * 2) + (self.teamwork * 2) + (
                                 self.vision * 2) + self.acceleration + self.agility + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def enganche(self):
        self.score = self.dribbling + (self.first_touch * 2) + (self.passing * 2) + (
                    self.technique * 2) + self.anticipation + (self.composure * 2) + (
                                 self.decisions * 2) + self.flair + self.off_the_ball + self.teamwork + (
                                 self.vision * 2) + self.agility + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def shadow_striker(self):
        self.score = (self.dribbling * 2) + (self.finishing * 2) + (
                    self.first_touch * 2) + self.passing + self.technique + (self.anticipation * 2) + (
                                 self.composure * 2) + self.concentration + self.decisions + (
                                 self.off_the_ball * 2) + self.work_rate + (
                                 self.acceleration * 2) + self.agility + self.balance + self.pace + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def attacking_midfielder_a(self):
        self.score = (self.dribbling * 2) + self.finishing + (self.first_touch * 2) + (self.long_shots * 2) + (
                    self.passing * 2) + (self.technique * 2) + (self.anticipation * 2) + self.composure + (
                                 self.decisions * 2) + (self.flair * 2) + (
                                 self.off_the_ball * 2) + self.vision + self.agility + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def advanced_forward(self):
        self.score = (self.dribbling * 2) + (self.finishing * 2) + (
                    self.first_touch * 2) + self.passing + (self.technique * 2) + self.anticipation + (
                                 self.composure * 2) + self.decisions + (
                                 self.off_the_ball * 2) + self.work_rate + (
                                 self.acceleration * 2) + self.agility + self.balance + self.pace + self.stamina + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def pressing_forward_d(self):
        self.score = self.first_touch + (self.aggression * 2) + (self.anticipation * 2) + (
                    self.bravery * 2) + self.composure + self.concentration + (self.decisions * 2) + (self.teamwork * 2) + (self.work_rate * 2) + (
                                 self.acceleration * 2) + self.agility + self.balance + (self.pace * 2) + (
                                 self.stamina * 2) + self.strength + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def pressing_forward_s(self):
        self.score = self.first_touch + self.passing + (self.aggression * 2) + (self.anticipation * 2) + (
                    self.bravery * 2) + self.composure + self.concentration + (self.decisions * 2) + self.off_the_ball + (self.teamwork * 2) + (self.work_rate * 2) + (
                                 self.acceleration * 2) + self.agility + self.balance + (self.pace * 2) + (
                                 self.stamina * 2) + self.strength + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def pressing_forward_a(self):
        self.score = self.finishing + self.first_touch + (self.aggression * 2) + (self.anticipation * 2) + (
                    self.bravery * 2) + self.composure + self.concentration + self.decisions + (
                                 self.off_the_ball * 2) + (self.teamwork * 2) + (self.work_rate * 2) + (
                                 self.acceleration * 2) + self.agility + self.balance + (self.pace * 2) + (
                                 self.stamina * 2) + self.strength + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def deep_lying_forward_s(self):
        self.score = self.finishing + (self.first_touch * 2) + (self.passing * 2) + (
                self.technique * 2) + self.anticipation + (self.composure * 2) + (
                             self.decisions * 2) + self.flair + (self.off_the_ball * 2) + (
                             self.teamwork * 2) + self.vision + self.balance + self.strength + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def deep_lying_forward_a(self):
        self.score = self.dribbling + self.finishing + (self.first_touch * 2) + (self.passing * 2) + (
                self.technique * 2) + self.anticipation + (self.composure * 2) + (
                             self.decisions * 2) + self.flair + (self.off_the_ball * 2) + (
                             self.teamwork * 2) + self.vision + self.balance + self.strength + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def complete_forward_s(self):
        self.score = (self.dribbling *2) + self.finishing + (self.first_touch * 2) + (self.heading * 2) + (self.long_shots * 2) + (self.passing * 2) + (self.technique * 2) + (self.anticipation * 2) + (self.composure * 2) + (self.decisions * 2) + (
                                 self.off_the_ball * 2) + self.teamwork + (self.vision * 2) + self.work_rate + (
                                 self.acceleration * 2) + (self.agility * 2) + self.balance + self.jumping_reach + self.pace + self.stamina + (self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def complete_forward_a(self):
        self.score = (self.dribbling *2) + (self.finishing * 2) + (self.first_touch * 2) + (self.heading * 2) + self.long_shots + self.passing + (self.technique * 2) + (self.anticipation * 2) + (self.composure * 2) + self.decisions + (
                                 self.off_the_ball * 2) + self.teamwork + self.vision + self.work_rate + (
                                 self.acceleration * 2) + (self.agility * 2) + self.balance + self.jumping_reach + self.pace + self.stamina + (self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def false_nine(self):
        self.score = (self.dribbling *2) + self.finishing + (self.first_touch * 2) + (self.passing * 2) + (self.technique * 2) + self.anticipation + (self.composure * 2) + (self.decisions * 2) + self.flair + (
                                 self.off_the_ball * 2) + self.teamwork + (self.vision * 2) + (
                                 self.acceleration * 2) + (self.agility * 2) + self.balance + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def poacher(self):
        self.score = (self.finishing * 2) + self.first_touch + self.technique + (self.anticipation * 2) + (self.composure * 2) + self.decisions + (self.off_the_ball * 2) + self.acceleration + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def target_forward_s(self):
        self.score = self.finishing + self.first_touch + (self.heading * 2) + self.aggression + self.anticipation + (self.bravery * 2) + self.composure + self.decisions + self.off_the_ball + (self.teamwork * 2) + (self.balance * 2) + (self.jumping_reach * 2) + (self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score

    def target_forward_a(self):
        self.score = (self.finishing * 2) + self.first_touch + (self.heading * 2) + self.aggression + self.anticipation + (self.bravery * 2) + (self.composure * 2) + self.decisions + (self.off_the_ball * 2) + self.teamwork + (self.balance * 2) + (self.jumping_reach * 2) + (self.strength * 2) + self.penalty_taking + self.free_kicks + self.corners + self.long_throws
        return self.score