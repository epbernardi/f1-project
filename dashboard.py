import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")

# Creating a sidebar
menu = st.sidebar.radio("Escolha uma página", ["Seasons 🏁", "Rankings 📊", "Interactions 📈"])

# Applying global CSS for black background, minha height and white text
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1A1A1A;  /* Cinza escuro */
        color: white;
    }
    .main .block-container {
        padding-top: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    div[data-testid="stDataFrame"] {
        min-height: 400px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Reading Data
df_drivers = pd.read_csv("df_drivers.csv")
df_teams = pd.read_csv("df_teams.csv")
df_fastest_laps = pd.read_csv("df_fastest_laps.csv")
df_races = pd.read_csv("df_races.csv")

# Seasons page on sidebar
if menu == "Seasons 🏁":
    st.title("Formula 1 Dataset 🏎️")
    st.write("Season by season")

    # Filter for the years
    selected_year = st.selectbox("Select the year", df_races["Year"].unique())

    # Selecting from the DFs by the selected year
    df_drivers_filtered = df_drivers[df_drivers["Year"] == selected_year]
    df_teams_filtered = df_teams[df_teams["Year"] == selected_year]
    df_fastest_laps_filtered = df_fastest_laps[df_fastest_laps["Year"] == selected_year]
    df_races_filtrered = df_races[df_races["Year"] == selected_year]

    # Create 3 columns for the rankings
    col1, col2, col3 = st.columns([3, 3, 3])

    # Drivers rankings
    with col1:
        st.subheader(f"Drivers Ranking ({selected_year}) 🏆")
        df_drivers_rank = df_drivers_filtered[["Driver", "Pts"]].sort_values(by="Pts", ascending=False)
        st.dataframe(df_drivers_rank, use_container_width=True, hide_index=True, height=450)

    # Teams Ranking
    with col2:
        st.subheader(f"Teams Ranking ({selected_year}) 🏁")
        df_teams_rank = df_teams_filtered[["Team", "Pts"]].sort_values(by="Pts", ascending=False)
        st.dataframe(df_teams_rank, use_container_width=True, hide_index=True, height=450)

    # Fastest Laps Ranking
    with col3:
        st.subheader(f"Fastest Laps ({selected_year}) ⚡")
        df_fastest_filtered = df_fastest_laps_filtered[["Grand Prix", "Driver", "Time"]]
        st.dataframe(df_fastest_filtered, use_container_width=True, hide_index=True, height=450)

    # Additional statistics
    st.subheader("Highlights of the Year 🎖")

    # 1. Driver with the most wins
    if "Winner" in df_races_filtrered.columns:
        driver_most_wins = df_races_filtrered["Winner"].value_counts().idxmax()
        races_won = df_races_filtrered["Winner"].value_counts().max()
    else:
        driver_most_wins, races_won = "Dados não disponíveis", "-"

    # 2. Driver with the most points
    if "Driver" in df_drivers_filtered.columns and "Pts" in df_drivers_filtered.columns:
        driver_most_points = df_drivers_filtered.groupby("Driver")["Pts"].sum().idxmax()
        qt_points = df_drivers_filtered.groupby("Driver")["Pts"].sum().max()
    else:
        driver_most_points, qt_points = "Dados não disponíveis", "-"

    # 3. Longest race
    if "Time" in df_races_filtrered.columns:
        df_races_filtrered["Time_seconds"] = pd.to_timedelta(df_races_filtrered["Time"], errors='coerce').dt.total_seconds()
        longest_race = df_races_filtrered.loc[df_races_filtrered["Time_seconds"].idxmax(), "Grand Prix"]
        longest_time = df_races_filtrered["Time"].max()
    else:
        longest_race, longest_time = "Dados não disponíveis", "-"

    # 4. Driver with the most fastest laps
    if "Driver" in df_fastest_laps_filtered.columns:
        driver_most_fastestlaps = df_fastest_laps_filtered["Driver"].value_counts().idxmax()
        qt_fastest_laps = df_fastest_laps_filtered["Driver"].value_counts().max()
    else:
        driver_most_fastestlaps, qt_fastest_laps = "Dados não disponíveis", "-"

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="Driver with the most wins", value=driver_most_wins, delta=f"{races_won} wins")

    with col2:
        st.metric(label="Driver with the most points", value=driver_most_points, delta=f"{qt_points} points")

    with col3:
        st.metric(label="Longest race", value=longest_race, delta=f"{longest_time}")

    with col4:
        st.metric(label="Driver with the most fastest laps", value=driver_most_fastestlaps, delta=f"{qt_fastest_laps} fastest laps")

# Página de Outro Projeto
elif menu == "Rankings 📊":
    st.title("Rankings 📊")
    st.write("Rankings of F1 history")

     # Criando colunas para os rankings
    col1, col2, col3 = st.columns([3, 3, 3])

    # Piloto que mais venceu corridas
    with col1:
        st.subheader("Most Winning Drivers 🏆")
        if "Winner" in df_races.columns:
            df_wins = df_races["Winner"].value_counts().reset_index()
            df_wins.columns = ["Driver", "Wins"]
            st.dataframe(df_wins, use_container_width=True, hide_index=True, height=450)
        else:
            st.write("Data not available")

    # Corridas mais disputadas
    with col2:
        st.subheader("Most Held Races 🏁")
        if "Grand Prix" in df_races.columns:
            df_gp_count = df_races["Grand Prix"].value_counts().reset_index()
            df_gp_count.columns = ["Grand Prix", "Times Held"]
            st.dataframe(df_gp_count, use_container_width=True, hide_index=True, height=450)
        else:
            st.write("Data not available")

    # Pilotos com mais voltas rápidas
    with col3:
        st.subheader("Fastest Lap Masters ⚡")
        if "Driver" in df_fastest_laps.columns:
            df_fastest_drivers = df_fastest_laps["Driver"].value_counts().reset_index()
            df_fastest_drivers.columns = ["Driver", "Fastest Laps"]
            st.dataframe(df_fastest_drivers, use_container_width=True, hide_index=True, height=450)
        else:
            st.write("Data not available")

    # Criando nova linha de rankings
    col4, col5 = st.columns([3, 3])

     # Piloto que mais pontuou
    with col4:
        st.subheader("Drivers with Most Points 🎯")
        if "Driver" in df_drivers.columns and "Pts" in df_drivers.columns:
            df_total_points = df_drivers.groupby("Driver")["Pts"].sum().reset_index()
            df_total_points = df_total_points.sort_values(by="Pts", ascending=False)
            st.dataframe(df_total_points, use_container_width=True, hide_index=True, height=450)
        else:
            st.write("Data not available")

    # Tempo total de corrida por pista (com média de tempo por corrida)
    with col5:
        st.subheader("Total Race Time by Track ⏱️")
    
        if "Grand Prix" in df_races.columns and "Time" in df_races.columns:
            # Converter a coluna "Time" para segundos
            df_races["Time_seconds"] = pd.to_timedelta(df_races["Time"], errors='coerce').dt.total_seconds()

            # Remover valores nulos que podem causar erro na agregação
            df_races = df_races.dropna(subset=["Time_seconds"])

            # Agrupar por "Grand Prix" e calcular o tempo total e a quantidade de corridas
            df_total_time = df_races.groupby("Grand Prix").agg(
                Total_Time=("Time_seconds", "sum"),
                Races_Competed=("Grand Prix", "count")  # Quantidade de vezes que a pista foi usada
            ).reset_index()

            # Calcular a média de tempo por corrida
            df_total_time["Avg_Time_per_Race"] = df_total_time["Total_Time"] / df_total_time["Races_Competed"]

            # Converter para formato legível de horas:minutos:segundos
            df_total_time["Total Time"] = df_total_time["Total_Time"].apply(
                lambda x: f"{int(x // 3600):02}:{int((x % 3600) // 60):02}:{int(x % 60):02}"
            )
            df_total_time["Avg Time per Race"] = df_total_time["Avg_Time_per_Race"].apply(
                lambda x: f"{int(x // 3600):02}:{int((x % 3600) // 60):02}:{int(x % 60):02}"
            )

            # Ordenar pelo tempo total de forma decrescente
            df_total_time = df_total_time.sort_values(by="Total_Time", ascending=False)

            # Exibir no Streamlit apenas as colunas formatadas
            st.dataframe(df_total_time[["Grand Prix", "Total Time", "Avg Time per Race"]],
                     use_container_width=True, hide_index=True, height=450)
        else:
            st.write("Data not available")


elif menu == "Interactions 📈":
    st.title("Interactions 📈")
    st.write("Explore a little of F1 history interactively.")

    # Verificando se as colunas necessárias existem
    if all(col in df_races.columns for col in ["Grand Prix", "Winner", "Year", "Time"]):
        # Criando lista de GPs ordenados alfabeticamente
        gp_sorted = sorted(df_races["Grand Prix"].unique())
        selected_gp = st.selectbox("Select a Grand Prix", gp_sorted)

        # Filtrando apenas as corridas desse GP
        df_gp = df_races[df_races["Grand Prix"] == selected_gp]

        # Contando quantas vezes cada piloto venceu esse GP
        df_gp_wins = df_gp["Winner"].value_counts().reset_index()
        df_gp_wins.columns = ["Driver", "Wins"]
        df_gp_wins = df_gp_wins.sort_values(by="Wins", ascending=True)  # Ordenação crescente no gráfico

        # Criando gráfico de vitórias por piloto no GP selecionado
        fig_gp_wins = px.bar(
            df_gp_wins,
            x="Wins",
            y="Driver",
            orientation="h",
            title=f"Drivers Wins in {selected_gp}",
            labels={"Wins": "Races Won", "Driver": "Pilot"},
            text="Wins",
            height=500
        )
        fig_gp_wins.update_traces(marker_color="blue", textposition="outside")

        st.plotly_chart(fig_gp_wins, use_container_width=True)

        # Criando lista de pilotos ordenados alfabeticamente
        drivers_sorted = sorted(df_gp_wins["Driver"].unique())
        selected_driver = st.selectbox("Select a Driver", drivers_sorted)

        # Filtrando os anos em que o piloto venceu nesse GP
        df_driver_gp = df_gp[df_gp["Winner"] == selected_driver][["Grand Prix", "Year", "Winner"]]
        df_driver_gp["Year"] = df_driver_gp["Year"].astype(str)  # Garantindo que o ano fique no formato correto

        # Obtendo a volta mais rápida nos anos das vitórias do piloto
        if "Grand Prix" in df_races.columns and "Year" in df_races.columns:
            # Mesclar df_races com df_fastest_laps para obter a volta mais rápida correta
            df_fastest_lap = df_fastest_laps[["Grand Prix", "Year", "Driver", "Time"]]
            df_fastest_lap["Year"] = df_fastest_lap["Year"].astype(str)  # Garantindo formato de string

            # Juntando as informações para exibir o desempenho do piloto vencedor e a volta mais rápida
            df_result = df_driver_gp.merge(df_fastest_lap, on=["Grand Prix", "Year"], how="left")
            df_result = df_result.rename(columns={"Driver": "Fastest Lap Driver"})  # Renomeando a coluna
            df_result = df_result.rename(columns={"Time": "Fastest Lap Time"})  # Renomeando a coluna
            df_result = df_result.sort_values(by="Year", ascending=True)

            # Exibir a tabela corrigida com a volta mais rápida correta
            st.subheader(f"Performances during {selected_driver} wins in {selected_gp}")
            st.dataframe(df_result, use_container_width=True, hide_index=True, height=200)

        # Ranking das 5 voltas mais rápidas já feitas nesse GP
        if "Time" in df_fastest_laps.columns:
            df_fastest_overall = df_fastest_laps[df_fastest_laps["Grand Prix"] == selected_gp][["Year", "Driver", "Time"]].copy()
            df_fastest_overall["Year"] = df_fastest_overall["Year"].astype(str)  # Ajustando formato do ano
            df_fastest_overall = df_fastest_overall.sort_values(by="Time", ascending=True).head(5)  # 5 melhores tempos

            # Exibir o ranking das voltas mais rápidas em formato de tabela
            st.subheader(f"Top 5 Fastest Laps in {selected_gp}")
            st.dataframe(df_fastest_overall, use_container_width=True, hide_index=True, height=200)  # Altura fixa para scroll

    else:
        st.write("Data not available. Ensure the dataset has 'Grand Prix', 'Winner', 'Year', and 'Time' columns.")
