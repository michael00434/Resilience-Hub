# Resilience Hub

Resilience Hub is a Python and Flet mobile app concept that brings practical community resilience guidance together in one place. It focuses on everyday preparation for heat, water interruptions, household resource use, and community information.

## Features

- **Community Updates:** sample update cards for demonstrating the experience. They are not live incident reports.
- **Essential Resources:** a resource directory screen. No verified local service or water-point listings are configured in this demo.
- **Save Smart:** general household energy and resource-saving tips. The app does not measure use or calculate actual savings.
- **HeatSafe:** practical hot-weather preparation, hydration, cooling, and heat-illness guidance. This guidance is available offline.
- **WaterWise:** household water conservation, leak planning, safe storage, and interruption preparation. This guidance is available offline.
- **No Water? Get Support:** safe-water advice and forms for describing an outage or requesting community assistance.

## Demo limitations

This project is a standalone demo with no backend or connected municipal/community-service integration. Community updates are sample content, and the resource directory has no verified listings. The app does not provide live weather or service alerts, locate active water supplies, or send outage reports or assistance requests. Submitted forms are kept in memory for the current app session only; they are not transmitted and are lost when the app closes. The app does not issue tracking numbers or confirm that a service received a request.

Treat the guidance as general information. Follow current instructions from local authorities and emergency services for your area.

## Technologies

- Python
- Flet 1.0.4 (pinned in `pyproject.toml`)
- Flet's Flutter-based tooling for platform builds

The top-level `assets/` directory contains the images used by the Flet app.

## Run locally

Create and activate a virtual environment, install the pinned app dependency, and run the Flet entry point.

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install flet==1.0.4
flet run main.py
```

To preview in a browser, use:

```powershell
flet run --web main.py
```

Use a Python version supported by Flet 1.0.4. Android packaging additionally requires a compatible Java JDK and Android SDK configured for the Flet/Flutter toolchain.

## Project files

- `main.py` — app screens, navigation, guidance, and session-only demo forms
- `pyproject.toml` — project metadata and Flet dependency/configuration
- `assets/` — app images
