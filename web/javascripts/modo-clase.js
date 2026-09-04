(() => {
  const storageKey = "dam-si-modo-clase";

  function setMode(enabled, button) {
    document.body.classList.toggle("class-mode", enabled);
    button.setAttribute("aria-pressed", String(enabled));
    button.title = enabled
      ? "Salir del modo clase (tecla M)"
      : "Ampliar la teoría y ocultar los laterales (tecla M)";
    button.querySelector("span").textContent = enabled
      ? "Salir del modo clase"
      : "Modo clase";
    localStorage.setItem(storageKey, enabled ? "1" : "0");
  }

  function installButton() {
    if (document.querySelector(".class-mode-button")) return;

    const button = document.createElement("button");
    button.type = "button";
    button.className = "class-mode-button";
    button.setAttribute("aria-label", "Alternar modo clase");
    button.innerHTML = `
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="M4 3h16a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2h-6v2h3v2H7v-2h3v-2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2m0 2v11h16V5H4Z"/>
      </svg>
      <span>Modo clase</span>`;
    document.body.appendChild(button);

    setMode(localStorage.getItem(storageKey) === "1", button);
    button.addEventListener("click", () => {
      setMode(!document.body.classList.contains("class-mode"), button);
    });

    document.addEventListener("keydown", (event) => {
      const target = event.target;
      const writing = target instanceof HTMLInputElement ||
        target instanceof HTMLTextAreaElement || target?.isContentEditable;
      if (!writing && event.key.toLowerCase() === "m") {
        setMode(!document.body.classList.contains("class-mode"), button);
      }
      if (event.key === "Escape" && document.body.classList.contains("class-mode")) {
        setMode(false, button);
      }
    });
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(installButton);
  } else {
    document.addEventListener("DOMContentLoaded", installButton);
  }
})();
