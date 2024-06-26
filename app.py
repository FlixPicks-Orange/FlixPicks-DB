from flask import render_template, redirect, url_for, session, jsonify, request
import pandas as pd
import config
import userdata.users as users
import userdata.subscriptions as subscriptions
import userdata.watch_history as watch_history
import userdata.recommendations as recommendations
import userdata.user_ratings as user_ratings
import content.movies as movies
import content.providers as providers
import content.genres as genres
import content.movie_genres as movie_genres
import content.movie_providers as movie_providers
import simulations.userdata as usersim
import simulations.watchhistory
import simulations.recommendations
import simulations.user_ratings
import userdata.user_clicks as clicks
import userdata.user_reactions as reactions
import userdata.watch_history as watch_history

import simulations.user_reactions as user_reactions
app = config.connex_app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/test")
def testing():
    user_reactions.simulate_user_reactions(10, 20)
    return "done"


@app.route("/Tables")
def all_tables():
    return render_template("all_tables.html")


@app.route("/Tables/Users")
def show_users():
    table_data = users.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["id", "username", "fname", "lname", "role", "email", "registration_date", "last_login", "password"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Users", path="/api/users")


@app.route("/Tables/Subscriptions")
def show_subscriptions():
    table_data = subscriptions.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["id", "user_id", "provider_id"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Subscriptions", path="/api/subscriptions")


@app.route("/Tables/WatchHistory")
def show_watch_history():
    table_data = watch_history.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["id", "user_id", "movie_id", "provider_id", "watched", "from_recommended", "supressed"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Watch History", path="/api/watch_history")


@app.route("/Tables/Recommendations")
def show_recommendations():
    table_data = recommendations.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["id", "user_id", "movie_id","title", "recommended"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Recommendations", path="/api/recommendations")


@app.route("/Tables/User_Ratings")
def show_user_ratings():
    table_data = user_ratings.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["id", "user_id", "movie_id", "user_liked"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="User Ratings", path="/api/user_ratings")


@app.route("/Tables/User_Clicks")
def show_user_clicks():
    table_data = clicks.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["id", "user_id", "page_id", "click_num", "timestamp"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="User Clicks", path="/api/user_clicks")


@app.route("/Tables/User_Reactions")
def show_user_reactions():
    table_data = reactions.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["id", "user_id", "movie_id", "reaction", "timestamp", "date"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="User Reactions", path="/api/reactions")


@app.route("/Tables/Movies")
def show_movies():
    table_data = movies.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["movie_id", "tmdb_id", "title", "release_date", "runtime", "poster_path", "backdrop_path", "language"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Movies", path="/api/subscriptions")


@app.route("/Tables/Providers")
def show_providers():
    table_data = providers.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["provider_id", "tmdb_id", "provider_name", "display_priority", "logo_path", "region"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Streaming Providers", path="/api/providers")


@app.route("/Tables/Genres")
def show_genres():
    table_data = genres.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["genre_id", "tmdb_id", "genre_name"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Genres", path="/api/genres")


@app.route("/Tables/Movie-Genres")
def show_movie_genres():
    table_data = movie_genres.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["id", "genre_id", "movie_id"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Movie Genres", path="/api/movies/all_genres")


@app.route("/Tables/Movie-Providers")
def show_movie_providers():
    table_data = movie_providers.show_all()
    df = pd.DataFrame(table_data)
    df = df.reindex(columns=["id", "provider_id", "movie_id", "link"])
    table_html = df.to_html(classes=["table", "table-bordered", "table-striped"], index=False)
    return render_template("display_table.html", table_html = table_html, table_name="Movie Providers", path="/api/movies/all_providers")


@app.route("/Simulation")
def simulation():
    if(session.get("sim_result")):
        result = session.get("sim_result")
        session["sim_result"] = None
    else: result = None
    return render_template("simulation.html", result=result)


@app.route("/Simulation/Users", methods=['GET', 'POST'])
def simulation_users():
    if request.method == 'POST':
        count = usersim.generate(int(request.form['NumUsers']))
        if(count > 0): session["sim_result"] = { "error": False, "message": str(count) + " simulated users added!" }
        else: session["sim_result"] = { "error": True, "message": "No simulated users added!" }
    else:
        session["sim_result"] = { "error": True, "message": "Unable to generate simulated users!" }
    return redirect(url_for('simulation'))


@app.route("/Simulation/WatchHistory", methods=['GET', 'POST'])
def simulation_watch_history():
    if request.method == 'POST':
        Operation = request.form['Operation']
        MinEntries = int(request.form['MinEntries'])
        MaxEntries = int(request.form['MaxEntries'])
        ProbFrequency = int(request.form['ProbFrequency'])
        session["sim_result"] = simulations.watchhistory.run_simulation(Operation, MinEntries, MaxEntries, ProbFrequency)
    else:
        session["sim_result"] = { "error": True, "message": "Unable to generate simulated Watch History!" }
    return redirect(url_for('simulation'))


@app.route("/Simulation/WatchHistory/Clear")
def clear_watch_history():
    simulations.watchhistory.clear()
    session["sim_result"] = { "error": False, "message": "Watch History Cleared" }
    return redirect(url_for('simulation'))


@app.route("/Simulation/Recommendations", methods=['GET', 'POST'])
def simulation_recommendations():
    if request.method == 'POST':
        simulations.recommendations.generate(int(request.form['NumRec']))
        session["sim_result"] = { "error": False, "message": "Simulated Recommendations Populated!" }
    else:
        session["sim_result"] = { "error": True, "message": "Unable to generate simulated users!" }
    return redirect(url_for('simulation'))


@app.route("/Simulation/Recommendations/Clear")
def clear_recommendations():
    simulations.recommendations.clear()
    session["sim_result"] = { "error": False, "message": "Recommendations Cleared" }
    return redirect(url_for('simulation'))


@app.route("/Simulation/UserRatings", methods=['GET', 'POST'])
def simulation_user_ratings():
    if request.method == 'POST':
        ProbRating = int(request.form['ProbRating'])
        ProbLikes = int(request.form['ProbLikes'])
        session["sim_result"] = simulations.user_ratings.run_simulation(ProbRating, ProbLikes)
    else:
        session["sim_result"] = { "error": True, "message": "Unable to generate simulated Watch History!" }
    return redirect(url_for('simulation'))


@app.route("/Simulation/UserRatings/Clear")
def clear_user_ratings():
    simulations.user_ratings.clear()
    session["sim_result"] = { "error": False, "message": "User Ratings Cleared" }
    return redirect(url_for('simulation'))


@app.route("/Import")
def import_data():
    return render_template("import_data.html")


if __name__ == "__main__":
    app.add_api(
        config.basedir / "swagger.yml",
        options={
            "swagger_ui": True,
            "swagger_url": "/docs",
        },
    )
    app.run(host="0.0.0.0", port=3000, debug=False)