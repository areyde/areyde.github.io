---
layout: archive
title: '«Дети». Музыкальные эксперименты 🎵'
description: "Альбом, включающий в себя музыку, записанную Ярославом Голубевым с друзьями в 2017–2019 годах."
language: ru
permalink: /music/
author_profile: true
---

{% include base_path %}

Мы с моим другом всегда очень любили побренчать что-нибудь на укулеле и попеть какой-нибудь фолк, благо музыкальные вкусы у нас были очень похожие.
В 2017 году этот процесс стал чуть более системным после того, как мы целенаправленно провели мой день рождения, записывая всякие песни, а потом смонтировали и выложили это в интернет.
В течение двух лет после этого мы регулярно так собирались различными составами, играли, пели, веселились и оформляли это в альбомы — в общей сложности, целых четыре штуки. 
Кроме того, в качестве подарков своим самым близким людям я записал пару собственных песен более серьёзно и старательно.

В 2019 году всё это как-то естественным образом прекратилось. На прощание с этой эпохой я собрал в один финальный альбом все самые лучшие песни, что мы записали, — самые весёлые, бесшабашные, а также те, где мы хоть немного попадаем в ноты.
Альбом я назвал «Дети» — по одной из песен, но ещё и потому, что именно детьми мы тогда и были. Взрослая жизнь мне кажется намного более интересной, но я совершенно очарован нашим юношеским задором, энергией и уверенностью в себе. 
Внизу страницы представлена подробная информация о том, кто, когда и как в этом участвовал, но главное — вот сама наша музыка.

<span style="color: #8a0000"><i>Внимание: в некоторых песнях достаточно много мата! Как молоды мы были...</i></span>

<style>
.album-player,
.album-player * {
  box-sizing: border-box;
}

.album-player {
  margin: 1.5rem 0 2rem;
  border: 1px solid #e5e5e5;
  border-radius: 8px;
  overflow: hidden;
  background: #fff;
}

.album-header {
  display: grid;
  grid-template-columns: 200px minmax(0, 1fr);
  gap: 1.5rem;
  padding: 1.25rem;
  border-bottom: 1px solid #eaeaea;
}

.album-cover {
  display: block;
  width: 100%;
  max-width: 200px;
  height: auto;
  margin: 0;
  border-radius: 5px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
}

.album-info {
  min-width: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.album-title {
  margin: 0 0 0.25rem;
  font-size: 1.55rem;
  line-height: 1.2;
}

.album-meta {
  margin-bottom: 1rem;
  color: #7a8288;
  font-size: 0.9rem;
}

.album-now-playing {
  min-height: 3.4rem;
  margin: 0.25rem 0 0.8rem;
}

.album-now-label {
  display: block;
  margin-bottom: 0.15rem;
  color: #7a8288;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

#album-now-title {
  display: block;
  font-size: 1rem;
}

#album-now-lineup {
  display: block;
  margin-top: 0.1rem;
  color: #7a8288;
  font-size: 0.8rem;
}

.album-transport-row {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
}

.album-control-button {
  width: 40px;
  height: 40px;
  padding: 0;
  border: 1px solid #ddd;
  border-radius: 50%;
  background: #f5f5f5;
  color: #333;
  cursor: pointer;
  font: inherit;
  font-size: 1rem;
  line-height: 1;
}

.album-control-button:hover {
  background: #e9e9e9;
}

.album-play-button {
  width: 46px;
  height: 46px;
  background: #3f4245;
  color: #fff;
  border-color: #3f4245;
  font-size: 1.15rem;
}

.album-play-button:hover {
  background: #222;
}

.album-volume-control {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  margin-left: auto;
}

.album-volume-button {
  border: 0;
  padding: 0.3rem;
  background: transparent;
  cursor: pointer;
  font-size: 1rem;
}

#album-volume {
  width: 75px;
}

.album-seek-row {
  display: grid;
  grid-template-columns: 38px minmax(0, 1fr) 38px;
  align-items: center;
  gap: 0.6rem;
  font-size: 0.75rem;
  color: #666;
  font-variant-numeric: tabular-nums;
}

.album-seek {
  width: 100%;
  margin: 0;
  cursor: pointer;
  accent-color: #555;
}

.album-side + .album-side {
  border-top: 1px solid #ddd;
}

.album-side-heading {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding: 0.7rem 1rem;
  background: #fafafa;
  border-bottom: 1px solid #ededed;
}

.album-side-title {
  font-weight: 700;
  font-size: 0.85rem;
  letter-spacing: 0.03em;
}

.album-side-stats {
  color: #888;
  font-size: 0.72rem;
  font-variant-numeric: tabular-nums;
}

.album-columns,
.album-track {
  display: grid;
  grid-template-columns:
    30px
    minmax(95px, 0.95fr)
    minmax(165px, 1.6fr)
    minmax(130px, 1.2fr)
    50px;
  gap: 0.7rem;
  align-items: center;
}

.album-columns {
  padding: 0.55rem 1rem;
  color: #777;
  border-bottom: 1px solid #ededed;
  font-size: 0.67rem;
  text-transform: uppercase;
  letter-spacing: 0.025em;
}

.album-track {
  width: 100%;
  padding: 0.65rem 1rem;
  border: 0;
  border-bottom: 1px solid #f0f0f0;
  background: #fff;
  color: inherit;
  text-align: left;
  cursor: pointer;
  font: inherit;
  font-size: 0.84rem;
}

.album-track:last-child {
  border-bottom: 0;
}

.album-track:hover {
  background: #f8f8f8;
}

.album-track.is-active {
  background: #f1f2f3;
}

.album-track.is-active .track-title {
  font-weight: 700;
}

.track-number {
  color: #888;
  text-align: center;
  font-variant-numeric: tabular-nums;
}

.track-lineup,
.track-original {
  min-width: 0;
  color: #555;
  overflow-wrap: anywhere;
}

.track-name-wrap {
  min-width: 0;
}

.track-title {
  display: block;
  font-weight: 600;
  overflow-wrap: anywhere;
}

.track-mobile-meta {
  display: none;
}

.track-duration {
  text-align: right;
  color: #555;
  font-variant-numeric: tabular-nums;
}

.album-noscript {
  margin: 1rem 0;
}

@media (max-width: 767px) {
  .album-header {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .album-cover {
    max-width: 280px;
    margin: 0 auto;
  }

  .album-title,
  .album-meta,
  .album-now-playing {
    text-align: center;
  }

  .album-transport-row {
    justify-content: center;
  }

  .album-volume-control {
    display: none;
  }

  .album-columns {
    display: none;
  }

  .album-track {
    grid-template-columns: 28px minmax(0, 1fr) 46px;
    gap: 0.5rem;
    padding: 0.7rem 0.8rem;
  }

  .track-lineup,
  .track-original {
    display: none;
  }

  .track-mobile-meta {
    display: block;
    margin-top: 0.12rem;
    color: #888;
    font-size: 0.7rem;
    font-weight: 400;
  }

  .album-side-heading {
    padding-left: 0.8rem;
    padding-right: 0.8rem;
  }
}

.album-cover-standalone {
  display: block;
  width: 65%;
  max-width: 700px;
  height: auto;
  margin: 1rem auto;
}

@media (max-width: 767px) {
  .album-cover-standalone {
    width: 100%;
  }
}
</style>

<div class="album-player" id="music-album">

  <div class="album-header">

    <div>
      <img
        class="album-cover"
        src="/images/album_cover.jpg"
        alt="Обложка музыкального альбома «Дети», нарисованная мелками на обоях."
      >
    </div>

    <div class="album-info">

      <h2 class="album-title">Дети</h2>

      <div class="album-meta">
        Ярослав Голубев <i>et al.</i> · 2019 ·
        <span id="album-total">15 треков · 54:29</span>
      </div>

      <div class="album-now-playing">
        <span class="album-now-label">Сейчас играет</span>
        <strong id="album-now-title">Песня про всё (Песня про Пашу)</strong>
        <span id="album-now-lineup">Ярослав Голубев</span>
      </div>

      <div class="album-transport-row">

        <button
          type="button"
          class="album-control-button"
          id="album-prev"
          aria-label="Предыдущий трек"
          title="Предыдущий трек"
        >⏮</button>

        <button
          type="button"
          class="album-control-button album-play-button"
          id="album-play"
          aria-label="Играть"
          title="Играть"
        >▶</button>

        <button
          type="button"
          class="album-control-button"
          id="album-next"
          aria-label="Следующий трек"
          title="Следующий трек"
        >⏭</button>

        <div class="album-volume-control">
          <button
            type="button"
            class="album-volume-button"
            id="album-mute"
            aria-label="Выключить звук"
            title="Выключить звук"
          >🔊</button>

          <input
            type="range"
            id="album-volume"
            min="0"
            max="1"
            step="0.05"
            value="1"
            aria-label="Громкость"
          >
        </div>

      </div>

      <div class="album-seek-row">
        <span id="album-current-time">0:00</span>

        <input
          type="range"
          class="album-seek"
          id="album-seek"
          min="0"
          max="1000"
          value="0"
          aria-label="Движение по треку"
        >

        <span id="album-track-length">5:40</span>
      </div>

    </div>
  </div>

<audio id="album-audio" preload="metadata"></audio>


  <section class="album-side">

    <div class="album-side-heading">
      <span class="album-side-title">Сторона 1</span>
      <span class="album-side-stats">9 треков · 27:19</span>
    </div>

    <div class="album-columns" aria-hidden="true">
      <span>#</span>
      <span>Состав</span>
      <span>Название</span>
      <span>Оригинальный исполнитель</span>
      <span>Дл.</span>
    </div>


    <button
      type="button"
      class="album-track"
      data-number="1"
      data-src="/music/01. Ярослав Голубев - Песня про всё (Песня про Пашу).mp3"
    >
      <span class="track-number">1</span>
      <span class="track-lineup">Ярослав Голубев</span>
      <span class="track-name-wrap">
        <span class="track-title">Песня про всё (Песня про Пашу)</span>
        <span class="track-mobile-meta">Ярослав Голубев</span>
      </span>
      <span class="track-original">Ярослав Голубев</span>
      <span class="track-duration">5:40</span>
    </button>


    <button
      type="button"
      class="album-track"
      data-number="2"
      data-src="/music/02. 33-43-31 - And I Love Her.mp3"
    >
      <span class="track-number">2</span>
      <span class="track-lineup">33:43:31</span>
      <span class="track-name-wrap">
        <span class="track-title">And I Love Her</span>
        <span class="track-mobile-meta">The Beatles</span>
      </span>
      <span class="track-original">The Beatles</span>
      <span class="track-duration">2:40</span>
    </button>


    <button
      type="button"
      class="album-track"
      data-number="3"
      data-src="/music/03. Братья Элвгрены - Лето.mp3"
    >
      <span class="track-number">3</span>
      <span class="track-lineup">Братья Элвгрены</span>
      <span class="track-name-wrap">
        <span class="track-title">Лето</span>
        <span class="track-mobile-meta">Майк Науменко</span>
      </span>
      <span class="track-original">Майк Науменко</span>
      <span class="track-duration">2:20</span>
    </button>


    <button
      type="button"
      class="album-track"
      data-number="4"
      data-src="/music/04. 33-43-31 - Give Peace a Chance.mp3"
    >
      <span class="track-number">4</span>
      <span class="track-lineup">33:43:31</span>
      <span class="track-name-wrap">
        <span class="track-title">Give Peace a Chance</span>
        <span class="track-mobile-meta">Plastic Ono Band</span>
      </span>
      <span class="track-original">Plastic Ono Band</span>
      <span class="track-duration">3:43</span>
    </button>


    <button
      type="button"
      class="album-track"
      data-number="5"
      data-src="/music/05. Страница 245 - Папа, твой сын никем не хочет быть.mp3"
    >
      <span class="track-number">5</span>
      <span class="track-lineup">Страница 245</span>
      <span class="track-name-wrap">
        <span class="track-title">Папа, твой сын никем не хочет быть</span>
        <span class="track-mobile-meta">Кино</span>
      </span>
      <span class="track-original">Кино</span>
      <span class="track-duration">2:10</span>
    </button>


    <button
      type="button"
      class="album-track"
      data-number="6"
      data-src="/music/06. 33-43-31 - Across the Universe.mp3"
    >
      <span class="track-number">6</span>
      <span class="track-lineup">33:43:31</span>
      <span class="track-name-wrap">
        <span class="track-title">Across the Universe</span>
        <span class="track-mobile-meta">The Beatles</span>
      </span>
      <span class="track-original">The Beatles</span>
      <span class="track-duration">3:52</span>
    </button>


    <button
      type="button"
      class="album-track"
      data-number="7"
      data-src="/music/07. Братья Элвгрены - Сельва.mp3"
    >
      <span class="track-number">7</span>
      <span class="track-lineup">Братья Элвгрены</span>
      <span class="track-name-wrap">
        <span class="track-title">Сельва</span>
        <span class="track-mobile-meta">Сергей Курёхин</span>
      </span>
      <span class="track-original">Сергей Курёхин</span>
      <span class="track-duration">2:28</span>
    </button>


    <button
      type="button"
      class="album-track"
      data-number="8"
      data-src="/music/08. Ярослав Голубев - Крюкообразность.mp3"
    >
      <span class="track-number">8</span>
      <span class="track-lineup">Ярослав Голубев</span>
      <span class="track-name-wrap">
        <span class="track-title">Крюкообразность</span>
        <span class="track-mobile-meta">Аквариум</span>
      </span>
      <span class="track-original">Аквариум</span>
      <span class="track-duration">1:36</span>
    </button>


    <button
      type="button"
      class="album-track"
      data-number="9"
      data-src="/music/09. Страница 245 - Марш советских танкистов.mp3"
    >
      <span class="track-number">9</span>
      <span class="track-lineup">Страница 245</span>
      <span class="track-name-wrap">
        <span class="track-title">Марш советских танкистов</span>
        <span class="track-mobile-meta">Пётр Киричек</span>
      </span>
      <span class="track-original">Пётр Киричек</span>
      <span class="track-duration">2:50</span>
    </button>

  </section>


  <section class="album-side">

    <div class="album-side-heading">
      <span class="album-side-title">Сторона 2</span>
      <span class="album-side-stats">6 треков · 27:10</span>
    </div>

    <div class="album-columns" aria-hidden="true">
      <span>#</span>
      <span>Состав</span>
      <span>Название</span>
      <span>Оригинальный исполнитель</span>
      <span>Дл.</span>
    </div>


    <button
      type="button"
      class="album-track"
      data-number="10"
      data-src="/music/10. 33-43-31 - Метель.mp3"
    >
      <span class="track-number">10</span>
      <span class="track-lineup">33:43:31</span>
      <span class="track-name-wrap">
        <span class="track-title">Метель</span>
        <span class="track-mobile-meta">ДДТ</span>
      </span>
      <span class="track-original">ДДТ</span>
      <span class="track-duration">5:40</span>
    </button>


    <button
      type="button"
      class="album-track"
      data-number="11"
      data-src="/music/11. Страница 245 - Дети.mp3"
    >
      <span class="track-number">11</span>
      <span class="track-lineup">Страница 245</span>
      <span class="track-name-wrap">
        <span class="track-title">Дети</span>
        <span class="track-mobile-meta">Елена Свирипа</span>
      </span>
      <span class="track-original">Елена Свирипа</span>
      <span class="track-duration">2:07</span>
    </button>


    <button
      type="button"
      class="album-track"
      data-number="12"
      data-src="/music/12. 33-43-31 - Всё идёт по плану.mp3"
    >
      <span class="track-number">12</span>
      <span class="track-lineup">33:43:31</span>
      <span class="track-name-wrap">
        <span class="track-title">Всё идёт по плану</span>
        <span class="track-mobile-meta">Гражданская оборона</span>
      </span>
      <span class="track-original">Гражданская оборона</span>
      <span class="track-duration">3:57</span>
    </button>


    <button
      type="button"
      class="album-track"
      data-number="13"
      data-src="/music/13. Братья Элвгрены - Алюминиевые огурцы.mp3"
    >
      <span class="track-number">13</span>
      <span class="track-lineup">Братья Элвгрены</span>
      <span class="track-name-wrap">
        <span class="track-title">Алюминиевые огурцы</span>
        <span class="track-mobile-meta">Кино</span>
      </span>
      <span class="track-original">Кино</span>
      <span class="track-duration">2:52</span>
    </button>


    <button
      type="button"
      class="album-track"
      data-number="14"
      data-src="/music/14. 33-43-31 - Twist and Shout.mp3"
    >
      <span class="track-number">14</span>
      <span class="track-lineup">33:43:31</span>
      <span class="track-name-wrap">
        <span class="track-title">Twist and Shout</span>
        <span class="track-mobile-meta">The Beatles</span>
      </span>
      <span class="track-original">The Beatles</span>
      <span class="track-duration">2:06</span>
    </button>


    <button
      type="button"
      class="album-track"
      data-number="15"
      data-src="/music/15. Ярослав Голубев - Елизавета.mp3"
    >
      <span class="track-number">15</span>
      <span class="track-lineup">Ярослав Голубев</span>
      <span class="track-name-wrap">
        <span class="track-title">Елизавета</span>
        <span class="track-mobile-meta">Ярослав Голубев</span>
      </span>
      <span class="track-original">Ярослав Голубев</span>
      <span class="track-duration">10:28</span>
    </button>

  </section>

</div>


<noscript>
  <div class="album-noscript">
    <p>JavaScript отключён. Записи также доступны напрямую:</p>

    <ol>
      <li><a href="/music/01. Ярослав Голубев - Песня про всё (Песня про Пашу).mp3">Песня про всё (Песня про Пашу)</a></li>
      <li><a href="/music/02. 33-43-31 - And I Love Her.mp3">And I Love Her</a></li>
      <li><a href="/music/03. Братья Элвгрены - Лето.mp3">Лето</a></li>
      <li><a href="/music/04. 33-43-31 - Give Peace a Chance.mp3">Give Peace a Chance</a></li>
      <li><a href="/music/05. Страница 245 - Папа, твой сын никем не хочет быть.mp3">Папа, твой сын никем не хочет быть</a></li>
      <li><a href="/music/06. 33-43-31 - Across the Universe.mp3">Across the Universe</a></li>
      <li><a href="/music/07. Братья Элвгрены - Сельва.mp3">Сельва</a></li>
      <li><a href="/music/08. Ярослав Голубев - Крюкообразность.mp3">Крюкообразность</a></li>
      <li><a href="/music/09. Страница 245 - Марш советских танкистов.mp3">Марш советских танкистов</a></li>
      <li><a href="/music/10. 33-43-31 - Метель.mp3">Метель</a></li>
      <li><a href="/music/11. Страница 245 - Дети.mp3">Дети</a></li>
      <li><a href="/music/12. 33-43-31 - Всё идёт по плану.mp3">Всё идёт по плану</a></li>
      <li><a href="/music/13. Братья Элвгрены - Алюминиевые огурцы.mp3">Алюминиевые огурцы</a></li>
      <li><a href="/music/14. 33-43-31 - Twist and Shout.mp3">Twist and Shout</a></li>
      <li><a href="/music/15. Ярослав Голубев - Елизавета.mp3">Елизавета</a></li>
    </ol>
  </div>
</noscript>

<script>
(function () {
  const root = document.getElementById("music-album");
  const audio = document.getElementById("album-audio");
  const tracks = Array.from(root.querySelectorAll(".album-track"));

  const playButton = document.getElementById("album-play");
  const prevButton = document.getElementById("album-prev");
  const nextButton = document.getElementById("album-next");
  const seek = document.getElementById("album-seek");
  const currentTime = document.getElementById("album-current-time");
  const trackLength = document.getElementById("album-track-length");
  const nowTitle = document.getElementById("album-now-title");
  const nowLineup = document.getElementById("album-now-lineup");
  const muteButton = document.getElementById("album-mute");
  const volume = document.getElementById("album-volume");
  const albumTotal = document.getElementById("album-total");

  const MIME = "audio/mpeg";
  const PREFETCH_AHEAD = 3;

  let useMSE =
    "MediaSource" in window &&
    MediaSource.isTypeSupported(MIME);

  let currentIndex = 0;
  let mse = null;
  let generation = 0;
  let directReady = false;

  function parseTime(text) {
    const parts = text.trim().split(":").map(Number);

    if (parts.length === 2) {
      return parts[0] * 60 + parts[1];
    }

    if (parts.length === 3) {
      return (
        parts[0] * 3600 +
        parts[1] * 60 +
        parts[2]
      );
    }

    return 0;
  }

  function formatTime(seconds) {
    if (
      !Number.isFinite(seconds) ||
      seconds < 0
    ) {
      return "0:00";
    }

    const whole = Math.floor(seconds);
    const hours = Math.floor(whole / 3600);
    const minutes =
      Math.floor((whole % 3600) / 60);
    const secs = whole % 60;

    if (hours > 0) {
      return (
        hours +
        ":" +
        String(minutes).padStart(2, "0") +
        ":" +
        String(secs).padStart(2, "0")
      );
    }

    return (
      minutes +
      ":" +
      String(secs).padStart(2, "0")
    );
  }

  function titleOf(index) {
    return tracks[index]
      .querySelector(".track-title")
      .textContent
      .trim();
  }

  function originalOf(index) {
    return tracks[index]
      .querySelector(".track-original")
      .textContent
      .trim();
  }

  function visibleDurationOf(index) {
    return tracks[index]
      .querySelector(".track-duration")
      .textContent
      .trim();
  }

  function plannedSeconds(index) {
    return parseTime(
      visibleDurationOf(index)
    );
  }

  function updateAlbumStatistics() {
    const total = tracks.reduce(
      function (sum, track) {
        return (
          sum +
          parseTime(
            track
              .querySelector(
                ".track-duration"
              )
              .textContent
          )
        );
      },
      0
    );

    albumTotal.textContent =
      tracks.length +
      " треков · " +
      formatTime(total);

    root
      .querySelectorAll(".album-side")
      .forEach(function (side) {
        const sideTracks = Array.from(
          side.querySelectorAll(
            ".album-track"
          )
        );

        const seconds =
          sideTracks.reduce(
            function (sum, track) {
              return (
                sum +
                parseTime(
                  track
                    .querySelector(
                      ".track-duration"
                    )
                    .textContent
                )
              );
            },
            0
          );

        const label =
          side.querySelector(
            ".album-side-stats"
          );

        label.textContent =
          sideTracks.length +
          " треков · " +
          formatTime(seconds);
      });
  }

  function updateRows() {
    tracks.forEach(
      function (track, index) {
        const number =
          track.querySelector(
            ".track-number"
          );

        const active =
          index === currentIndex;

        track.classList.toggle(
          "is-active",
          active
        );

        number.textContent =
          active
            ? "▶"
            : track.dataset.number;

        if (active) {
          track.setAttribute(
            "aria-current",
            "true"
          );
        } else {
          track.removeAttribute(
            "aria-current"
          );
        }
      }
    );
  }

  function updateMetadata() {
    nowTitle.textContent =
      titleOf(currentIndex);

    nowLineup.textContent =
      originalOf(currentIndex);

    if (
      !("mediaSession" in navigator)
    ) {
      return;
    }

    navigator.mediaSession.metadata =
      new MediaMetadata({
        title: titleOf(currentIndex),
        artist: originalOf(currentIndex),
        album: root
          .querySelector(".album-title")
          .textContent
          .trim(),
        artwork: [
          {
            src: new URL(
              "/images/album_cover.jpg",
              window.location.origin
            ).href
          }
        ]
      });
  }

  function updatePlayButton() {
    const paused = audio.paused;

    playButton.textContent =
      paused ? "▶" : "⏸";

    playButton.setAttribute(
      "aria-label",
      paused ? "Играть" : "Пауза"
    );

    playButton.setAttribute(
      "title",
      paused ? "Играть" : "Пауза"
    );

    if (
      "mediaSession" in navigator
    ) {
      navigator.mediaSession.playbackState =
        paused
          ? "paused"
          : "playing";
    }
  }

  function updateMuteButton() {
    const muted =
      audio.muted ||
      audio.volume === 0;

    muteButton.textContent =
      muted ? "🔇" : "🔊";

    muteButton.setAttribute(
      "aria-label",
      muted
        ? "Включить звук"
        : "Выключить звук"
    );

    muteButton.setAttribute(
      "title",
      muted
        ? "Включить звук"
        : "Выключить звук"
    );
  }

  function playAudio() {
    const promise = audio.play();

    if (
      promise &&
      typeof promise.catch === "function"
    ) {
      promise.catch(
        function (error) {
          console.error(
            "Не удалось начать воспроизведение:",
            error
          );
        }
      );
    }

    return promise;
  }

  function once(
    target,
    eventName
  ) {
    return new Promise(
      function (resolve, reject) {
        function ok(event) {
          cleanup();
          resolve(event);
        }

        function fail() {
          cleanup();

          reject(
            new Error(
              "Ошибка события " +
              eventName
            )
          );
        }

        function cleanup() {
          target.removeEventListener(
            eventName,
            ok
          );

          target.removeEventListener(
            "error",
            fail
          );
        }

        target.addEventListener(
          eventName,
          ok,
          { once: true }
        );

        target.addEventListener(
          "error",
          fail,
          { once: true }
        );
      }
    );
  }

  function bufferedEnd(state) {
    const ranges =
      state.buffer.buffered;

    return ranges.length
      ? ranges.end(
          ranges.length - 1
        )
      : 0;
  }

  async function newStream(
    startIndex
  ) {
    const myGeneration =
      ++generation;

    const mediaSource =
      new MediaSource();

    const objectUrl =
      URL.createObjectURL(
        mediaSource
      );

    const old = mse;

    const state = {
      generation: myGeneration,
      mediaSource: mediaSource,
      buffer: null,
      objectUrl: objectUrl,
      baseIndex: startIndex,
      nextIndex: startIndex,
      starts: {},
      ends: {},
      appendPromise:
        Promise.resolve()
    };

    mse = state;

    const opened = once(
      mediaSource,
      "sourceopen"
    );

    audio.src = objectUrl;

    await opened;

    if (
      mse !== state ||
      generation !== myGeneration
    ) {
      throw new Error(
        "Устаревшая MSE-сессия"
      );
    }

    state.buffer =
      mediaSource.addSourceBuffer(
        MIME
      );

    state.buffer.mode =
      "sequence";

    if (
      old &&
      old.objectUrl
    ) {
      URL.revokeObjectURL(
        old.objectUrl
      );
    }

    return state;
  }

  function appendTrack(
    state,
    index
  ) {
    state.appendPromise =
      state.appendPromise.then(
        async function () {
          if (
            mse !== state ||
            generation !==
              state.generation
          ) {
            return;
          }

          if (
            index !==
            state.nextIndex
          ) {
            return;
          }

          const response =
            await fetch(
              tracks[index]
                .dataset.src
            );

          if (!response.ok) {
            throw new Error(
              "HTTP " +
              response.status +
              " для " +
              tracks[index]
                .dataset.src
            );
          }

          const bytes =
            await response.arrayBuffer();

          if (
            mse !== state ||
            generation !==
              state.generation
          ) {
            return;
          }

          const start =
            bufferedEnd(state);

          state.buffer.appendBuffer(
            bytes
          );

          await once(
            state.buffer,
            "updateend"
          );

          if (
            mse !== state ||
            generation !==
              state.generation
          ) {
            return;
          }

          const end =
            bufferedEnd(state);

          if (!(end > start)) {
            throw new Error(
              "Трек " +
              (index + 1) +
              " не был добавлен в MSE"
            );
          }

          state.starts[index] =
            start;

          state.ends[index] =
            end;

          state.nextIndex =
            index + 1;

          if (
            index ===
              tracks.length - 1 &&
            state.mediaSource
              .readyState === "open"
          ) {
            state.mediaSource
              .endOfStream();
          }
        }
      );

    return state.appendPromise;
  }

  async function appendThrough(
    state,
    finalIndex
  ) {
    const limit = Math.min(
      finalIndex,
      tracks.length - 1
    );

    while (
      mse === state &&
      state.nextIndex <= limit
    ) {
      await appendTrack(
        state,
        state.nextIndex
      );
    }
  }

  function prefetch(
    state,
    index
  ) {
    if (
      !state ||
      mse !== state
    ) {
      return;
    }

    appendThrough(
      state,
      index + PREFETCH_AHEAD
    ).catch(
      function (error) {
        console.error(
          "Ошибка MSE-prefetch:",
          error
        );
      }
    );
  }

  function hasTrack(
    state,
    index
  ) {
    return (
      !!state &&
      Object.prototype
        .hasOwnProperty.call(
          state.starts,
          index
        )
    );
  }

  function trackStart() {
    if (
      useMSE &&
      hasTrack(
        mse,
        currentIndex
      )
    ) {
      return mse.starts[
        currentIndex
      ];
    }

    return 0;
  }

  function trackDuration() {
    if (
      useMSE &&
      hasTrack(
        mse,
        currentIndex
      ) &&
      Object.prototype
        .hasOwnProperty.call(
          mse.ends,
          currentIndex
        )
    ) {
      return (
        mse.ends[
          currentIndex
        ] -
        mse.starts[
          currentIndex
        ]
      );
    }

    if (
      !useMSE &&
      Number.isFinite(
        audio.duration
      ) &&
      audio.duration > 0
    ) {
      return audio.duration;
    }

    return plannedSeconds(
      currentIndex
    );
  }

  function localTime() {
    return Math.max(
      0,
      (audio.currentTime || 0) -
        trackStart()
    );
  }

  function updatePositionState() {
    if (
      !(
        "mediaSession" in
        navigator
      ) ||
      !(
        "setPositionState" in
        navigator.mediaSession
      )
    ) {
      return;
    }

    const duration =
      trackDuration();

    if (
      !Number.isFinite(
        duration
      ) ||
      duration <= 0
    ) {
      return;
    }

    const position =
      Math.min(
        Math.max(
          0,
          localTime()
        ),
        Math.max(
          0,
          duration - 0.001
        )
      );

    try {
      navigator.mediaSession
        .setPositionState({
          duration: duration,
          playbackRate:
            audio.playbackRate,
          position: position
        });
    } catch (error) {
    }
  }

  function commitTrack(index) {
    if (
      index < 0 ||
      index >= tracks.length
    ) {
      return;
    }

    currentIndex = index;

    updateRows();
    updateMetadata();

    trackLength.textContent =
      formatTime(
        trackDuration()
      );

    updatePositionState();
  }

  function trackForAbsoluteTime(
    time
  ) {
    if (!mse) {
      return currentIndex;
    }

    let result =
      currentIndex;

    for (
      let i = mse.baseIndex;
      i < mse.nextIndex;
      i += 1
    ) {
      if (
        !hasTrack(mse, i)
      ) {
        continue;
      }

      if (
        time + 0.03 >=
        mse.starts[i]
      ) {
        result = i;
      } else {
        break;
      }
    }

    return result;
  }

  async function selectMSE(
    index,
    autoplay
  ) {
    if (
      index < 0 ||
      index >= tracks.length
    ) {
      return;
    }

    let state = mse;

    if (
      !hasTrack(
        state,
        index
      )
    ) {
      state =
        await newStream(index);

      await appendThrough(
        state,
        index
      );
    }

    if (mse !== state) {
      return;
    }

    commitTrack(index);

    audio.currentTime =
      state.starts[index];

    currentTime.textContent =
      "0:00";

    seek.value = 0;

    prefetch(
      state,
      index
    );

    if (autoplay) {
      playAudio();
    }
  }

  function selectDirect(
    index,
    autoplay
  ) {
    if (
      index < 0 ||
      index >= tracks.length
    ) {
      return;
    }

    directReady = true;

    commitTrack(index);

    audio.src =
      tracks[index].dataset.src;

    currentTime.textContent =
      "0:00";

    seek.value = 0;

    if (autoplay) {
      playAudio();
    }
  }

  function selectTrack(
    index,
    autoplay
  ) {
    if (!useMSE) {
      selectDirect(
        index,
        autoplay
      );

      return;
    }

    selectMSE(
      index,
      autoplay
    ).catch(
      function (error) {
        console.error(
          "MSE не сработал; включён обычный режим:",
          error
        );

        useMSE = false;
        generation += 1;

        if (
          mse &&
          mse.objectUrl
        ) {
          URL.revokeObjectURL(
            mse.objectUrl
          );
        }

        mse = null;

        selectDirect(
          index,
          autoplay
        );
      }
    );
  }

  function nextTrack(
    autoplay
  ) {
    if (
      currentIndex <
      tracks.length - 1
    ) {
      selectTrack(
        currentIndex + 1,
        autoplay
      );
    } else {
      selectTrack(
        0,
        autoplay
      );
    }
  }

  function previousTrack(
    autoplay
  ) {
    if (localTime() > 3) {
      audio.currentTime =
        trackStart();

      if (autoplay) {
        playAudio();
      }

      return;
    }

    if (currentIndex > 0) {
      selectTrack(
        currentIndex - 1,
        autoplay
      );
    } else {
      selectTrack(
        tracks.length - 1,
        autoplay
      );
    }
  }

  function setMediaAction(
    name,
    handler
  ) {
    if (
      !("mediaSession" in navigator)
    ) {
      return;
    }

    try {
      navigator.mediaSession
        .setActionHandler(
          name,
          handler
        );
    } catch (error) {
    }
  }

  tracks.forEach(
    function (track, index) {
      track.addEventListener(
        "click",
        function () {
          if (
            index !==
            currentIndex
          ) {
            selectTrack(
              index,
              true
            );

            return;
          }

          const ready =
            useMSE
              ? hasTrack(
                  mse,
                  index
                )
              : directReady;

          if (!ready) {
            selectTrack(
              index,
              true
            );

            return;
          }

          if (audio.paused) {
            playAudio();
          } else {
            audio.pause();
          }
        }
      );
    }
  );

  playButton.addEventListener(
    "click",
    function () {
      const ready =
        useMSE
          ? hasTrack(
              mse,
              currentIndex
            )
          : directReady;

      if (!ready) {
        selectTrack(
          currentIndex,
          true
        );

        return;
      }

      if (audio.paused) {
        playAudio();
      } else {
        audio.pause();
      }
    }
  );

  prevButton.addEventListener(
    "click",
    function () {
      previousTrack(true);
    }
  );

  nextButton.addEventListener(
    "click",
    function () {
      nextTrack(true);
    }
  );

  seek.addEventListener(
    "input",
    function () {
      const duration =
        trackDuration();

      if (
        !Number.isFinite(
          duration
        ) ||
        duration <= 0
      ) {
        return;
      }

      const wanted =
        (
          Number(seek.value) /
          1000
        ) *
        duration;

      audio.currentTime =
        trackStart() +
        wanted;
    }
  );

  volume.addEventListener(
    "input",
    function () {
      audio.volume =
        Number(volume.value);

      audio.muted =
        audio.volume === 0;

      updateMuteButton();
    }
  );

  muteButton.addEventListener(
    "click",
    function () {
      audio.muted =
        !audio.muted;

      updateMuteButton();
    }
  );

  audio.addEventListener(
    "play",
    updatePlayButton
  );

  audio.addEventListener(
    "pause",
    updatePlayButton
  );

  audio.addEventListener(
    "loadedmetadata",
    function () {
      if (
        !useMSE &&
        Number.isFinite(
          audio.duration
        )
      ) {
        trackLength.textContent =
          formatTime(
            audio.duration
          );
      }

      updatePositionState();
    }
  );

  audio.addEventListener(
    "timeupdate",
    function () {
      if (
        useMSE &&
        mse
      ) {
        const detected =
          trackForAbsoluteTime(
            audio.currentTime
          );

        if (
          detected !==
          currentIndex
        ) {
          commitTrack(
            detected
          );

          prefetch(
            mse,
            detected
          );
        }
      }

      const position =
        localTime();

      const duration =
        trackDuration();

      currentTime.textContent =
        formatTime(
          position
        );

      trackLength.textContent =
        formatTime(
          duration
        );

      if (
        Number.isFinite(
          duration
        ) &&
        duration > 0
      ) {
        seek.value =
          Math.min(
            1000,
            Math.round(
              (
                position /
                duration
              ) *
              1000
            )
          );
      }

      updatePositionState();
    }
  );

  audio.addEventListener(
    "ended",
    function () {
      if (
        !useMSE &&
        currentIndex <
          tracks.length - 1
      ) {
        selectTrack(
          currentIndex + 1,
          true
        );

        return;
      }

      seek.value = 1000;

      updatePlayButton();

      if (
        "mediaSession" in
        navigator
      ) {
        navigator.mediaSession
          .playbackState =
          "none";
      }
    }
  );

  setMediaAction(
    "play",
    function () {
      const ready =
        useMSE
          ? hasTrack(
              mse,
              currentIndex
            )
          : directReady;

      if (ready) {
        playAudio();
      } else {
        selectTrack(
          currentIndex,
          true
        );
      }
    }
  );

  setMediaAction(
    "pause",
    function () {
      audio.pause();
    }
  );

  setMediaAction(
    "previoustrack",
    function () {
      previousTrack(true);
    }
  );

  setMediaAction(
    "nexttrack",
    function () {
      nextTrack(true);
    }
  );

  setMediaAction(
    "seekbackward",
    function (details) {
      const amount =
        details.seekOffset ||
        10;

      audio.currentTime =
        trackStart() +
        Math.max(
          0,
          localTime() -
            amount
        );
    }
  );

  setMediaAction(
    "seekforward",
    function (details) {
      const amount =
        details.seekOffset ||
        10;

      const duration =
        trackDuration();

      audio.currentTime =
        trackStart() +
        Math.min(
          duration,
          localTime() +
            amount
        );
    }
  );

  setMediaAction(
    "seekto",
    function (details) {
      if (
        typeof details.seekTime !==
        "number"
      ) {
        return;
      }

      const duration =
        trackDuration();

      const wanted =
        Math.max(
          0,
          Math.min(
            duration,
            details.seekTime
          )
        );

      const absolute =
        trackStart() +
        wanted;

      if (
        details.fastSeek &&
        typeof audio.fastSeek ===
          "function"
      ) {
        audio.fastSeek(
          absolute
        );
      } else {
        audio.currentTime =
          absolute;
      }
    }
  );

  updateAlbumStatistics();

  commitTrack(0);

  currentTime.textContent =
    "0:00";

  seek.value = 0;

  updatePlayButton();
  updateMuteButton();

  if (!useMSE) {
    console.info(
      "MSE audio/mpeg не поддерживается; используется обычный режим плеера."
    );
  }
})();
</script>

<h2>История записи</h2>

* **Апрель 2017**. На мой день рождения мы записали альбом **«77/78»**. С него взяты _«Метель»_ и _«Twist and Shout»_.
* **Ноябрь 2017**. Я записал _«Крюкообразность»_ (зачем-то).
* **Январь 2018**. На Новый год мы записали альбом **«Славься, Отечество!»**. С него взяты _«Across the Universe»_ и _«Всё идёт по плану»_.
* **Март 2018**. В подарок Паше на день рождения я записал _«Песню про всё (Песню про Пашу)»_. На праздновании самого дня рождения мы записали _«And I Love Her»_ и _«Give Peace a Chance»_.
* **Июль 2018**. На квартире сестры Паши мы записали альбом **«Лиговский, 53»**. С него взяты _«Лето»_, _«Сельва»_ и _«Алюминиевые огурцы»_.
* **Январь 2019**. В подарок Елизавете я записал, неожиданно, _«Елизавету»_.
* **Апрель 2019**. На мой день рождения мы записали **«Советский альбом»**. С него взяты _«Папа, твой сын никем не хочет быть»_, _«Марш советских танкистов»_ и _«Дети»_.

<h2>Обложка</h2>

Обложки для всех наших предыдущих альбомов я дизайнил сам, как попало. Но для собрания всего _лучшего_ нужно было что-то _особенное_. Был всего один человек, который мог мне помочь. 
Замечательная Елизавета (та самая, которой посвящена песня) пришла ко мне домой и нарисовала обложку прямо на моих обоях, мелками.

<img src="/images/album_cover.jpg" class="album-cover-standalone" title="Обложка альбома «Дети»" alt="Обложка альбома «Дети», которую мы нарисовали на обоях моей квартиры.">

Жизнь всех нас давно разбросала по самым разным занятиям и странам, но обложка всё так же держится в моём родительском доме, заставленная столом.

<h2>Участники записи</h2>

Несмотря на то, что песни записывались в разное время и в разных составах, а на некоторых записях на пьянках, мягко говоря, трудно понять, что вообще происходит, я всегда старался вести точные заметки (хотя бы на утро) и никого не забывать. 
Есть некая юношеская романтика в том, как много всего и как искренне мы туда намешали!

* **Ярослав** — вокал (1–4, 6–15), бэк-вокал (5), укулеле (3–7, 9, 10, 12–14), дарбука (1, 2, 7, 13), акустическая гитара (1, 8, 15), художественный свист (7, 13), маракасы (3), студия (1–6, 8–12, 14, 15), запись, монтаж.
* **Павел** — вокал (2, 4–6, 9, 10, 12, 14), бэк-вокал (3, 7, 13), укулеле (2, 6, 10, 12, 14), акустическая гитара (3, 5, 7, 9, 13), клаве (3), дарбука (4), бубен (4), студия (7, 13).
* **Александр I** — вокал (2, 4, 6, 10, 14), акустическая гитара (2, 4, 6, 10, 12, 14).
* **Ася** — бэк-вокал (2, 4, 6, 10, 12, 14), маракасы (4, 6, 12), техническая помощь (6, 10, 12, 14).
* **Елизавета** — вокал (9, 11), бэк-вокал (5), орехи (5, 9), дизайн обложки.
* **Александр II** — бэк-вокал (5, 9), дарбука (5, 9).
* **Елена** — бэк-вокал (5, 9).
* **Иван** — вокал (12), бэк-вокал (6), дарбука (6).
* **Илья** — вокал (12), бэк-вокал (6), маракасы (6, 12).
* **Андрей** — вокал (12), бэк-вокал (6), классическая гитара (12).
* **Михаил** — бэк-вокал (6, 12), маракасы (6, 12).
* **Александра** — бэк-вокал (6, 12).
* **Дарина** — бэк-вокал (6, 12).
* **Птицы (жёлтая и зелёная)** — бэк-вокал (7, 13).
* **[Камин](https://www.youtube.com/watch?v=mmBEZ3x-QRo)** — бэк-вокал (6, 12).