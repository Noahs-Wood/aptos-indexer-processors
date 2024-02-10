DROP INDEX IF EXISTS tournament_is_joinable;
DROP INDEX IF EXISTS tournament_coin_rewards_coin_type;
DROP INDEX IF EXISTS tournament_coin_rewards_coin_amount;
DROP INDEX IF EXISTS tournament_token_rewards_tokens;
DROP INDEX IF EXISTS tournament_current_round_number;
DROP INDEX IF EXISTS tournament_round_address;
DROP INDEX IF EXISTS tournament_room_round_address;
DROP INDEX IF EXISTS tournament_room_in_progress;
DROP INDEX IF EXISTS tournament_player_room_address;
DROP TABLE IF EXISTS tournament_token_owners;
DROP TABLE IF EXISTS tournament_players;
DROP TABLE IF EXISTS tournament_rooms;
DROP TABLE IF EXISTS tournament_rounds;
DROP TABLE IF EXISTS tournament_coin_rewards;
DROP TABLE IF EXISTS tournament_token_rewards;
DROP TABLE IF EXISTS tournaments;
-- MANUAL GAME INDEXING
DROP INDEX IF EXISTS rock_paper_scissors_games_player1_token_address;
DROP INDEX IF EXISTS rock_paper_scissors_games_player2_token_address;
DROP INDEX IF EXISTS trivia_questions_question;
DROP INDEX IF EXISTS trivia_questions_revealed_answer_index;
DROP INDEX IF EXISTS trivia_answers_answer_index;
DROP TABLE IF EXISTS rock_paper_scissors_games;
DROP TABLE IF EXISTS rock_paper_scissors_players;
DROP TABLE IF EXISTS trivia_questions;
DROP TABLE IF EXISTS trivia_answers;
