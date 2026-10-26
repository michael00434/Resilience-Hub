import flet as ft

# Resilience Hub demo: sample content only, with no live community backend.
BG = "#F6F1E7"
SURFACE = "#FFFDF8"
SURFACE_RAISED = "#EEF1E9"
BORDER = "#DFE3D9"
WHITE = "#FFFDF8"
CREAM = "#F6F1E7"
MUTED = "#667268"
INK = "#20362B"
GREEN = "#2F8054"
GREEN_DARK = "#205B3C"
TEAL = "#168F83"
TEAL_DARK = "#126D64"
GOLD = "#E8B94F"
ORANGE = "#B3472E"
ORANGE_TINT = "#F4E0D5"

VIEWS = ["updates", "resources", "save_smart"]


def main(page: ft.Page):
    page.title = "Resilience Hub"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = BG
    page.padding = 0
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(primary=ORANGE, secondary=GREEN)
    )

    def card(content, width=None, padding=18, bgcolor=SURFACE, border_color=BORDER):
        return ft.Container(
            content=content,
            width=width,
            padding=padding,
            bgcolor=bgcolor,
            border=ft.Border.all(1, border_color),
            border_radius=15,
        )

    def action_button(label, on_click, secondary=False, icon=None):
        return ft.Button(
            label,
            icon=icon,
            on_click=on_click,
            style=ft.ButtonStyle(
                color=GREEN_DARK if secondary else WHITE,
                bgcolor=SURFACE_RAISED if secondary else ORANGE,
                side=ft.BorderSide(1, GREEN_DARK if secondary else ORANGE),
                shape=ft.RoundedRectangleBorder(radius=12),
            ),
        )

    def go(view):
        render(view)

    def navigation_changed(e):
        index = e.control.selected_index
        if 0 <= index < len(VIEWS):
            go(VIEWS[index])

    def section_heading(title, description):
        return ft.Column(
            controls=[
                ft.Text(title, size=23, weight=ft.FontWeight.BOLD, color=GREEN_DARK),
                ft.Text(description, size=13, color=MUTED),
                ft.Container(width=34, height=3, bgcolor=ORANGE, border_radius=2),
            ],
            spacing=7,
        )

    def demo_badge(label="DEMO CONTENT", accent=GOLD):
        return ft.Container(
            content=ft.Text(
                label,
                size=9,
                weight=ft.FontWeight.BOLD,
                color=GREEN_DARK if accent in (GREEN, GREEN_DARK) else TEAL_DARK if accent == TEAL else INK,
            ),
            padding=ft.Padding.symmetric(horizontal=9, vertical=5),
            bgcolor="#E4EDE5" if accent in (GREEN, GREEN_DARK) else "#DCEEEA" if accent == TEAL else ORANGE_TINT if accent == ORANGE else "#F5EBCB",
            border_radius=7,
        )

    def photo(src, label, width, height):
        return ft.Image(
            src=src,
            width=width,
            height=height,
            fit=ft.BoxFit.COVER,
            border_radius=14,
            semantics_label=label,
            cache_width=960,
        )

    def home_screen(content_width):
        wide_layout = content_width >= 760
        if content_width >= 900:
            destination_width = (content_width - 24) / 3
        elif content_width >= 560:
            destination_width = (content_width - 12) / 2
        else:
            destination_width = content_width

        hero_copy = ft.Column(
            controls=[
                demo_badge("DEMO EXPERIENCE · NO LIVE SERVICES", accent=GOLD),
                ft.Text(
                    "PEOPLE · PLACE · PREPARATION",
                    size=10,
                    weight=ft.FontWeight.BOLD,
                    color=GOLD,
                ),
                ft.Text(
                    "Stronger communities start with everyday choices.",
                    size=35 if wide_layout else 28,
                    weight=ft.FontWeight.BOLD,
                    color=CREAM,
                ),
                ft.Text(
                    "Practical ideas for water, energy and household readiness.",
                    size=15,
                    color="#E5E9E1",
                ),
                action_button(
                    "No Water? Get Support",
                    on_click=lambda e: go("water_support"),
                    icon=ft.Icons.WATER_DROP_OUTLINED,
                ),
                action_button(
                    "Explore Save Smart",
                    on_click=lambda e: go("save_smart"),
                    icon=ft.Icons.ARROW_FORWARD,
                ),
            ],
            spacing=14,
            expand=True,
        )
        hero_photo = ft.Container(
            content=photo(
                "community-resilience-colour.jpg",
                "Neighbors tending a shared garden together; illustrative demo image",
                272 if wide_layout else content_width - 40,
                218 if wide_layout else 150,
            ),
            padding=4,
            bgcolor=GOLD,
            border_radius=18,
        )
        hero_content = (
            ft.Row(
                controls=[hero_copy, hero_photo],
                spacing=24,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
            if wide_layout
            else ft.Column(controls=[hero_photo, hero_copy], spacing=18)
        )

        destinations = [
            (
                "Community Updates",
                "A clearly labelled preview of how community reports could appear.",
                "community-resilience-colour.jpg",
                "Neighbors tending a shared garden together; illustrative demo image",
                ft.Icons.CAMPAIGN_OUTLINED,
                GREEN_DARK,
                "DEMO PREVIEW",
                "View updates",
                "updates",
            ),
            (
                "Essential Resources",
                "A sample space for practical, locally relevant support information.",
                "water-conservation-colour.jpg",
                "Reusable water container being filled from a tap; illustrative demo image",
                ft.Icons.VOLUNTEER_ACTIVISM_OUTLINED,
                TEAL_DARK,
                "DEMO DIRECTORY",
                "Open directory",
                "resources",
            ),
            (
                "Save Smart",
                "General water and energy ideas for everyday household readiness.",
                "energy-saving-colour.jpg",
                "Household light being switched off to save energy; illustrative demo image",
                ft.Icons.SAVINGS_OUTLINED,
                ORANGE,
                "GENERAL DEMO TIPS",
                "See general tips",
                "save_smart",
            ),
        ]
        destination_cards = []
        for title, description, src, alt, icon, accent, badge, button_label, view in destinations:
            destination_cards.append(
                card(
                    ft.Column(
                        controls=[
                            photo(src, alt, destination_width - 32, 118),
                            ft.Text(badge, size=9, weight=ft.FontWeight.BOLD, color=accent),
                            ft.Row(
                                controls=[
                                    ft.Icon(icon, color=accent, size=20),
                                    ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color=INK, expand=True),
                                ],
                                spacing=9,
                            ),
                            ft.Text(description, size=12, color=MUTED),
                            action_button(
                                button_label,
                                on_click=lambda e, target=view: go(target),
                                secondary=True,
                                icon=ft.Icons.ARROW_FORWARD,
                            ),
                        ],
                        spacing=10,
                    ),
                    width=destination_width,
                    padding=16,
                    border_color="#C9D7CA" if accent == GREEN_DARK else "#C7DDD8" if accent == TEAL_DARK else "#E8D0C4",
                )
            )

        tips_card = card(
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.WATER_DROP_OUTLINED, color=TEAL, size=21),
                            ft.Column(
                                controls=[
                                    ft.Text("Use water thoughtfully", size=14, weight=ft.FontWeight.BOLD, color=INK),
                                    ft.Text("Turn off taps when they are not in use.", size=12, color=MUTED),
                                ],
                                spacing=3,
                                expand=True,
                            ),
                            demo_badge("SAMPLE TIP", accent=TEAL),
                        ],
                        spacing=12,
                    ),
                    ft.Divider(color=BORDER, height=1),
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.ELECTRIC_BOLT, color=ORANGE, size=21),
                            ft.Column(
                                controls=[
                                    ft.Text("Reduce electricity use", size=14, weight=ft.FontWeight.BOLD, color=INK),
                                    ft.Text("Switch off lights and appliances when not needed.", size=12, color=MUTED),
                                ],
                                spacing=3,
                                expand=True,
                            ),
                            demo_badge("SAMPLE TIP", accent=ORANGE),
                        ],
                        spacing=12,
                    ),
                ],
                spacing=7,
            ),
            width=content_width,
            padding=16,
        )

        home_actions = card(
            ft.Column(
                controls=[
                    ft.Text("Prepare for heat and water disruptions", size=16, weight=ft.FontWeight.BOLD, color=INK),
                    ft.Text("Keep practical guidance close and find the right next step.", size=12, color=MUTED),
                    action_button("No Water? Get Support", on_click=lambda e: go("water_support"), icon=ft.Icons.WATER_DROP_OUTLINED),
                    action_button("HeatSafe · Hot weather guidance", on_click=lambda e: go("heat_safe"), secondary=True, icon=ft.Icons.INFO_OUTLINE),
                    action_button("WaterWise · Save and store water", on_click=lambda e: go("water_wise"), secondary=True, icon=ft.Icons.WATER_DROP_OUTLINED),
                ],
                spacing=10,
            ),
            width=content_width,
            padding=16,
            bgcolor="#F4E0D5",
            border_color="#E8C8B8",
        )

        return [
            card(
                hero_content,
                width=content_width,
                padding=26 if wide_layout else 16,
                bgcolor=GREEN_DARK,
                border_color=GREEN_DARK,
            ),
            home_actions,
            section_heading("Find your starting point", "Three parts of a more resilient everyday."),
            ft.Row(
                controls=destination_cards,
                wrap=True,
                spacing=12,
                run_spacing=12,
            ),
            section_heading("Quick ideas", "General examples from Save Smart."),
            tips_card,
            ft.Text(
                "Demo content only · No live reports, verified listings, weather, service status or actual savings are connected.",
                size=11,
                color=MUTED,
            ),
        ]

    def updates_screen(content_width):
        return [
            section_heading(
                "Community Updates",
                "A preview of how local disruption reports could be presented.",
            ),
            card(
                ft.Column(
                    controls=[
                        photo(
                            "community-resilience-colour.jpg",
                            "Neighbors tending a shared garden together; illustrative demo image",
                            content_width - 36,
                            164,
                        ),
                        demo_badge("DEMO SAMPLE · NOT A REAL INCIDENT"),
                        ft.Text("Example service update", size=17, weight=ft.FontWeight.BOLD, color=INK),
                        ft.Text(
                            "This placeholder is for demonstration only. Reports are not submitted "
                            "to or shared with a community service.",
                            size=13,
                            color=MUTED,
                        ),
                    ],
                    spacing=11,
                ),
            ),
            ft.Text(
                "Report submission and live community sharing are not implemented.",
                size=12,
                color=MUTED,
            ),
        ]

    def resources_screen():
        return [
            section_heading(
                "Essential Resources",
                "A space for practical, locally relevant support information.",
            ),
            card(
                ft.Column(
                    controls=[
                        demo_badge("DEMO DIRECTORY · NO VERIFIED LISTINGS"),
                        ft.Icon(ft.Icons.INFO_OUTLINE, color=TEAL, size=24),
                        ft.Text("No local resources have been verified for this demo.", color=INK),
                        ft.Text(
                            "Add trusted contact details and service information before relying on this directory.",
                            size=13,
                            color=MUTED,
                        ),
                    ],
                    spacing=11,
                ),
            ),
        ]

    def save_smart_screen(content_width):
        tips = [
            (
                "Switch off unused lights",
                "Turn off lights when leaving a room to reduce unnecessary electricity use.",
                "ENERGY",
                ft.Icons.ELECTRIC_BOLT,
                ORANGE,
            ),
            (
                "Check for leaking taps",
                "Repair or report dripping taps to help prevent water waste.",
                "WATER",
                ft.Icons.WATER_DROP_OUTLINED,
                TEAL,
            ),
            (
                "Use a bowl when washing vegetables",
                "Collect water in a bowl instead of leaving the tap running.",
                "WATER",
                ft.Icons.WATER_DROP_OUTLINED,
                TEAL,
            ),
            (
                "Wash full loads",
                "Run washing machines with full loads when practical to use water and electricity more efficiently.",
                "WATER & ENERGY",
                ft.Icons.ELECTRIC_BOLT,
                GREEN,
            ),
            (
                "Keep emergency water ready",
                "Store a safe supply of drinking water for service disruptions and follow local water-safety guidance.",
                "PREPAREDNESS",
                ft.Icons.INFO_OUTLINE,
                GOLD,
            ),
            (
                "Keep the fridge efficient",
                "Avoid leaving the fridge door open and check that it seals properly.",
                "ENERGY",
                ft.Icons.ELECTRIC_BOLT,
                ORANGE,
            ),
            (
                "Prepare a small outage kit",
                "Keep useful essentials together, such as a torch, spare batteries, a power bank and essential contact details.",
                "PREPAREDNESS",
                ft.Icons.INFO_OUTLINE,
                GOLD,
            ),
        ]
        tip_rows = []
        for index, (title, description, category, icon, accent) in enumerate(tips):
            if index:
                tip_rows.append(ft.Divider(color=BORDER, height=1))
            tip_rows.append(
                ft.Row(
                    controls=[
                        ft.Icon(icon, color=accent, size=21),
                        ft.Column(
                            controls=[
                                ft.Text(title, size=14, weight=ft.FontWeight.BOLD, color=INK),
                                ft.Text(description, size=12, color=MUTED),
                                demo_badge(f"{category} · SAMPLE TIP", accent=accent),
                            ],
                            spacing=5,
                            expand=True,
                        ),
                    ],
                    spacing=12,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                )
            )

        return [
            section_heading(
                "Save Smart",
                "Small household habits and simple preparation ideas.",
            ),
            card(
                ft.Column(
                    controls=[
                        demo_badge("7 GENERAL DEMO TIPS"),
                        photo(
                            "water-conservation-colour.jpg",
                            "Reusable water container being filled from a tap; illustrative demo image",
                            content_width - 36,
                            156,
                        ),
                        ft.Divider(color=BORDER),
                        photo(
                            "energy-saving-colour.jpg",
                            "Household light being switched off to save energy; illustrative demo image",
                            content_width - 36,
                            156,
                        ),
                        ft.Divider(color=BORDER),
                        *tip_rows,
                    ],
                    spacing=11,
                ),
                bgcolor="#EFF5EF",
                border_color="#C9D7CA",
            ),
        ]


    # Session-only records are intentionally not persisted or transmitted.
    session_records = []

    def info_card(title, bullets, icon, accent=TEAL, intro=None, bgcolor=SURFACE):
        rows = [
            ft.Row(
                controls=[
                    ft.Icon(icon, color=accent, size=21),
                    ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color=INK, expand=True),
                ],
                spacing=10,
            )
        ]
        if intro:
            rows.append(ft.Text(intro, size=12, color=MUTED))
        for item in bullets:
            rows.append(
                ft.Row(
                    controls=[
                        ft.Text("•", size=16, weight=ft.FontWeight.BOLD, color=accent),
                        ft.Text(item, size=13, color=INK, expand=True),
                    ],
                    spacing=8,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                )
            )
        return card(ft.Column(controls=rows, spacing=9), padding=16, bgcolor=bgcolor)

    def back_home_button():
        return action_button("Back to Home", on_click=lambda e: go("home"), secondary=True, icon=ft.Icons.HOME_OUTLINED)

    def heat_safe_screen():
        return [
            back_home_button(),
            section_heading("HeatSafe", "Practical steps for hot days. This guidance works offline."),
            info_card("Before the heat", [
                "Check local weather and heat-health notices; plan strenuous outdoor work for cooler hours.",
                "Prepare drinking water, light clothing, a charged phone, and a cooler room or nearby public place.",
                "Check in with children, older adults, people with disabilities or chronic conditions, and anyone living alone.",
                "Outdoor workers should agree on shade breaks, water access, lighter duties, and a way to call for help.",
            ], ft.Icons.INFO_OUTLINE, accent=GREEN),
            info_card("During hot weather", [
                "Rest in shade or a cool place, slow down, and take regular breaks.",
                "Drink water regularly; do not wait until you feel very thirsty. Follow a clinician's fluid advice if you have a medical fluid restriction.",
                "Headache, dizziness, weakness, nausea, intense thirst, or reduced urination can be warning signs. Rest somewhere cool, sip safe water if fully alert, and seek medical help if symptoms worsen or persist.",
                "Wear loose, light clothing and use a cool damp cloth or a cool shower when available.",
                "Never leave a child, dependent adult, or pet in a parked vehicle.",
            ], ft.Icons.INFO_OUTLINE, accent=TEAL),
            info_card("Keep your home cooler", [
                "Shade sun-facing windows with curtains, blinds, or a light-coloured covering during the hottest hours.",
                "Open windows for cross-ventilation when outside air is cooler and it is safe to do so.",
                "Limit oven use and other heat-producing activities; choose simple meals when practical.",
                "Use a fan when it helps you feel cooler; if the room is extremely hot, seek a cooler place rather than relying on a fan alone.",
            ], ft.Icons.HOME_OUTLINED, accent=GREEN),
            info_card("After heat exposure", [
                "Continue resting in a cool place and drink safe fluids if you are alert and not vomiting.",
                "Watch for worsening symptoms. Seek medical advice if symptoms persist or return.",
                "Check on vulnerable neighbours and family members after the hottest part of the day.",
            ], ft.Icons.INFO_OUTLINE, accent=TEAL),
            card(ft.Column(controls=[
                ft.Row(controls=[ft.Icon(ft.Icons.INFO_OUTLINE, color=ORANGE, size=22), ft.Text("Heat illness can become an emergency", size=16, weight=ft.FontWeight.BOLD, color=GREEN_DARK, expand=True)], spacing=9),
                ft.Text("Confusion, slurred speech, seizures, collapse or loss of consciousness, or very hot skin can signal heat stroke. Call your local emergency medical number immediately.", size=13, color=INK),
                ft.Text("While help is coming: move the person to shade or a cool place, loosen unnecessary clothing, wet the skin or apply cool wet cloths, and fan them. Stay with them. Do not give anything to drink if they are confused, having a seizure, or unconscious.", size=13, color=INK),
            ], spacing=10), padding=16, bgcolor=ORANGE_TINT, border_color="#E8C8B8"),
            ft.Text("General guidance adapted from WHO and CDC public-health advice. Follow local health guidance; this app is not a medical diagnosis.", size=11, color=MUTED),
        ]

    def water_wise_screen():
        return [
            back_home_button(),
            section_heading("WaterWise", "Save water, plan ahead, and protect stored supplies — available offline."),
            info_card("Use less at home", [
                "Fix or report dripping taps, running toilets, and visible leaks promptly.",
                "Turn taps off while brushing teeth or soaping dishes; use a basin for washing vegetables.",
                "Run washing machines with full loads when practical and choose shorter showers.",
                "Use leftover clean rinse water for suitable non-drinking tasks, such as watering ornamental plants.",
            ], ft.Icons.WATER_DROP_OUTLINED, accent=TEAL),
            info_card("Prevent leaks and plan use", [
                "Check meters, taps, toilet cisterns, and exposed pipes for unexpected changes or damp patches.",
                "Know where the household shut-off valve is and how to use it safely.",
                "Plan for drinking, food preparation, essential hygiene, and care needs during an interruption.",
                "Keep official municipal service contacts and outage notices somewhere accessible offline.",
            ], ft.Icons.INFO_OUTLINE, accent=GREEN),
            info_card("Store water safely", [
                "Use a clean, food-safe container with a tight lid; never reuse containers that held fuel, pesticides, or other chemicals.",
                "Keep containers covered, cool, and out of direct sunlight. Label drinking water and the date it was stored.",
                "Pour water or use a clean tap; do not dip hands, cups, or utensils into stored water.",
                "Follow local health instructions for how much to store, how long to keep it, and whether treatment is required.",
            ], ft.Icons.INFO_OUTLINE, accent=TEAL),
            info_card("Prepare for an interruption", [
                "Follow official notices about timing, collection points, and water-use instructions.",
                "Fill clean, covered containers before a planned interruption if local guidance advises it.",
                "Keep a reserve for drinking, food preparation, essential medicines, and hygiene; consider vulnerable household members.",
                "If service stops unexpectedly, contact the municipality or water provider through its official service channels.",
            ], ft.Icons.INFO_OUTLINE, accent=GREEN),
            card(ft.Text("Safety warning: Do not assume water from a tank, stream, borehole, rain collection, or an unverified collection point is safe to drink. Use water confirmed safe by local authorities or follow official treatment guidance. Water exposed to fuel or toxic chemicals may not be made safe by boiling.", size=13, color=INK), padding=16, bgcolor=ORANGE_TINT, border_color="#E8C8B8"),
            ft.Text("General household guidance adapted from CDC safe-water storage and emergency-water advice. Local water-quality directions take priority.", size=11, color=MUTED),
        ]

    def water_support_screen():
        area_field = ft.TextField(label="Affected area", hint_text="Suburb, village, or nearest landmark")
        duration_field = ft.TextField(label="How long has water been unavailable?", hint_text="For example, since this morning")
        problem_field = ft.Dropdown(label="Problem type", options=[
            ft.DropdownOption(key="no_supply", text="No water supply"),
            ft.DropdownOption(key="low_pressure", text="Very low pressure"),
            ft.DropdownOption(key="quality", text="Water looks or smells unusual"),
            ft.DropdownOption(key="leak", text="Burst pipe or visible leak"),
            ft.DropdownOption(key="other", text="Other water-service problem"),
        ])
        description_field = ft.TextField(label="Description", hint_text="What is happening? Avoid sensitive information.", multiline=True, min_lines=3, max_lines=5)
        outage_contact = ft.TextField(label="Contact details (optional)", hint_text="Only include details you are comfortable keeping on this device")
        outage_status = ft.Text("", size=12, color=GREEN_DARK)
        need_area = ft.TextField(label="General area", hint_text="Suburb, village, or nearest landmark")
        need_description = ft.TextField(label="What help is needed?", hint_text="Describe the water assistance needed and any access constraints.", multiline=True, min_lines=3, max_lines=5)
        need_priority = ft.Dropdown(label="Priority", value="standard", options=[
            ft.DropdownOption(key="standard", text="Standard request"),
            ft.DropdownOption(key="urgent", text="Urgent — vulnerable resident or immediate need"),
        ])
        need_contact = ft.TextField(label="Contact details (optional)", hint_text="Only include details you are comfortable keeping on this device")
        need_status = ft.Text("", size=12, color=GREEN_DARK)
        history = ft.Column(spacing=5)

        def refresh_history():
            history.controls.clear()
            if not session_records:
                history.controls.append(ft.Text("No requests recorded in this app session yet.", size=12, color=MUTED))
                return
            history.controls.append(ft.Text(f"{len(session_records)} session-only request(s). Nothing here has been sent to a service.", size=12, weight=ft.FontWeight.BOLD, color=GREEN_DARK))
            for record in session_records[-5:]:
                urgency = " · URGENT" if record.get("priority") == "urgent" else ""
                history.controls.append(ft.Text(f"{record['kind']}: {record['area']}{urgency}", size=12, color=INK))

        def submit_outage(e):
            area = (area_field.value or "").strip()
            duration = (duration_field.value or "").strip()
            problem = problem_field.value
            description = (description_field.value or "").strip()
            area_field.error_text = None if area else "Enter the affected area."
            duration_field.error_text = None if duration else "Enter an approximate duration."
            problem_field.error_text = None if problem else "Choose a problem type."
            description_field.error_text = None if description else "Describe the issue."
            if not all([area, duration, problem, description]):
                page.update()
                return
            session_records.append({"kind": "Water outage report", "area": area, "detail": problem, "duration": duration, "description": description, "contact": (outage_contact.value or "").strip(), "priority": ""})
            outage_status.value = "Recorded in this app's memory for this open session only. It is not saved after closing or sent to your municipality or any service."
            area_field.error_text = duration_field.error_text = problem_field.error_text = description_field.error_text = None
            refresh_history()
            page.update()

        def submit_assistance(e):
            area = (need_area.value or "").strip()
            description = (need_description.value or "").strip()
            need_area.error_text = None if area else "Enter a general area."
            need_description.error_text = None if description else "Describe the assistance needed."
            if not area or not description:
                page.update()
                return
            session_records.append({"kind": "Community water assistance request", "area": area, "description": description, "contact": (need_contact.value or "").strip(), "priority": need_priority.value or "standard"})
            need_status.value = "Recorded in this app's memory for this open session only. It is not saved after closing or sent to a community responder."
            need_area.error_text = need_description.error_text = None
            refresh_history()
            page.update()

        refresh_history()
        return [
            back_home_button(),
            section_heading("No Water? Get Support", "Choose a next step. This demo has no live water-point directory or reporting service."),
            info_card("Find Water", [
                "No verified water collection points are configured in this app, so it cannot direct you to a safe supply.",
                "Contact your municipality or water provider through its official website or service number and ask about confirmed collection points, hours, and household limits.",
                "Check official municipal notices or trusted local community channels, then confirm water is intended for drinking before using it.",
            ], ft.Icons.INFO_OUTLINE, accent=ORANGE, intro="Directory status: no verified locations available.", bgcolor=ORANGE_TINT),
            info_card("Safe Water Advice", [
                "Use only water confirmed safe by local officials, sealed drinking water, or water treated according to official local directions.",
                "Store safe water in a clean, covered, food-safe container and pour it out without touching the water.",
                "Do not drink from an unverified point or assume clear-looking water is safe. Boiling does not remove fuel or toxic chemical contamination.",
                "Wash hands with safe water and soap where available; keep containers and dispensing areas clean.",
            ], ft.Icons.WATER_DROP_OUTLINED, accent=TEAL),
            card(ft.Column(controls=[
                ft.Text("Report a Water Outage", size=17, weight=ft.FontWeight.BOLD, color=GREEN_DARK),
                ft.Text("Enter an area, duration, problem type, and description. Submitting creates a session-only note on this device; it does not contact a municipality.", size=12, color=MUTED),
                area_field, duration_field, problem_field, description_field, outage_contact,
                action_button("Record outage note", on_click=submit_outage, icon=ft.Icons.INFO_OUTLINE),
                outage_status,
            ], spacing=10), padding=16),
            card(ft.Column(controls=[
                ft.Text("Request Community Assistance", size=17, weight=ft.FontWeight.BOLD, color=GREEN_DARK),
                ft.Text("Include a general area and what support is needed. Choose urgent if a vulnerable resident or immediate need is involved.", size=12, color=MUTED),
                need_area, need_description, need_priority, need_contact,
                action_button("Record assistance note", on_click=submit_assistance, secondary=True, icon=ft.Icons.VOLUNTEER_ACTIVISM_OUTLINED),
                need_status,
            ], spacing=10), padding=16),
            card(ft.Column(controls=[
                ft.Text("This session's local notes", size=15, weight=ft.FontWeight.BOLD, color=INK),
                ft.Text("Notes stay in memory only while the app is open. They are not durable case records; do not enter sensitive personal or medical details.", size=12, color=MUTED),
                history,
            ], spacing=8), padding=16, bgcolor="#EFF5EF", border_color="#C9D7CA"),
        ]

    current_view = "home"

    def render(view="home"):
        nonlocal current_view
        current_view = view
        page.controls.clear()
        window_width = page.width or 1200
        desktop_navigation = window_width >= 1100
        shell_width = max(280, min(1380, window_width - 32))
        main_panel_width = shell_width - 268 if desktop_navigation else shell_width
        content_width = max(220, main_panel_width - 48)
        if desktop_navigation or view == "home" or view not in VIEWS:
            page.navigation_bar = None
        else:
            page.navigation_bar = ft.NavigationBar(
                destinations=[
                    ft.NavigationBarDestination(
                        icon=ft.Icons.CAMPAIGN_OUTLINED,
                        selected_icon=ft.Icons.CAMPAIGN,
                        label="Community Updates",
                    ),
                    ft.NavigationBarDestination(
                        icon=ft.Icons.VOLUNTEER_ACTIVISM_OUTLINED,
                        selected_icon=ft.Icons.VOLUNTEER_ACTIVISM,
                        label="Essential Resources",
                    ),
                    ft.NavigationBarDestination(
                        icon=ft.Icons.SAVINGS_OUTLINED,
                        selected_icon=ft.Icons.SAVINGS,
                        label="Save Smart",
                    ),
                ],
                selected_index=VIEWS.index(view),
                on_change=navigation_changed,
                bgcolor=SURFACE,
                indicator_color=ORANGE_TINT,
                elevation=0,
            )

        header = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Icon(ft.Icons.ECO_OUTLINED, color=GREEN_DARK, size=23),
                                padding=10,
                                bgcolor="#E4EDE5",
                                border_radius=12,
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text("RESILIENCE HUB", size=12, weight=ft.FontWeight.BOLD, color=GREEN_DARK),
                                    ft.Text("Community care, made practical", size=12, color=MUTED),
                                ],
                                spacing=2,
                            ),
                        ],
                        spacing=12,
                    ),
                    on_click=lambda e: go("home"),
                    tooltip="Home",
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.INFO_OUTLINE, size=16, color=ORANGE),
                            ft.Text(
                                "DEMO MODE · Preview content only; no live services are connected.",
                                size=10,
                                weight=ft.FontWeight.W_600,
                                color=GREEN_DARK,
                                expand=True,
                            ),
                        ],
                        spacing=8,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=ft.Padding.symmetric(horizontal=11, vertical=8),
                    bgcolor=ORANGE_TINT,
                    border_radius=9,
                ),
            ],
            spacing=10,
        )

        if view == "home":
            content = home_screen(content_width)
        elif view == "updates":
            content = updates_screen(content_width)
        elif view == "resources":
            content = resources_screen()
        elif view == "save_smart":
            content = save_smart_screen(content_width)
        elif view == "heat_safe":
            content = heat_safe_screen()
        elif view == "water_wise":
            content = water_wise_screen()
        elif view == "water_support":
            content = water_support_screen()
        else:
            content = home_screen(content_width)

        main_panel = ft.Container(
            content=ft.Column(
                controls=[header, ft.Divider(color=BORDER), *content],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            ),
            width=main_panel_width,
            padding=24 if desktop_navigation else 20,
        )

        if desktop_navigation:
            nav_entries = [
                ("Home", ft.Icons.HOME_OUTLINED, "home"),
                ("Community Updates", ft.Icons.CAMPAIGN_OUTLINED, "updates"),
                ("Essential Resources", ft.Icons.VOLUNTEER_ACTIVISM_OUTLINED, "resources"),
                ("Save Smart", ft.Icons.ENERGY_SAVINGS_LEAF_OUTLINED, "save_smart"),
                ("HeatSafe", ft.Icons.INFO_OUTLINE, "heat_safe"),
                ("WaterWise", ft.Icons.WATER_DROP_OUTLINED, "water_wise"),
                ("No Water? Get Support", ft.Icons.VOLUNTEER_ACTIVISM_OUTLINED, "water_support"),
            ]
            sidebar_items = []
            for label, icon, target in nav_entries:
                selected = view == target
                sidebar_items.append(
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Icon(icon, size=19, color=GREEN_DARK if selected else MUTED),
                                ft.Text(
                                    label,
                                    size=13,
                                    weight=ft.FontWeight.W_600 if selected else ft.FontWeight.NORMAL,
                                    color=GREEN_DARK if selected else MUTED,
                                ),
                            ],
                            spacing=12,
                        ),
                        padding=ft.Padding.symmetric(horizontal=13, vertical=12),
                        bgcolor="#E4EDE5" if selected else None,
                        border_radius=12,
                        on_click=lambda e, destination=target: go(destination),
                    )
                )
            sidebar = ft.Container(
                content=ft.Column(
                    controls=[
                        *sidebar_items,
                        ft.Container(expand=True),
                        card(
                            ft.Column(
                                controls=[
                                    ft.Icon(ft.Icons.ENERGY_SAVINGS_LEAF_OUTLINED, color=GREEN, size=22),
                                    ft.Text(
                                        "Small actions. Stronger communities.",
                                        size=13,
                                        weight=ft.FontWeight.BOLD,
                                        color=INK,
                                    ),
                                    ft.Text(
                                        "Use less. Spend less. Be better prepared.",
                                        size=11,
                                        color=MUTED,
                                    ),
                                ],
                                spacing=8,
                            ),
                            padding=14,
                        ),
                    ],
                    spacing=10,
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                ),
                width=244,
                height=page.height or 820,
                padding=20,
                bgcolor=SURFACE,
                border=ft.Border.all(1, BORDER),
                border_radius=20,
            )
            page_content = ft.Row(
                controls=[sidebar, main_panel],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.START,
                expand=True,
            )
        else:
            page_content = ft.Container(
                content=main_panel,
                width=shell_width,
            )

        page.add(
            ft.Row(
                controls=[page_content],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.START,
                expand=True,
            )
        )
        page.update()

    page.on_resize = lambda e: render(current_view)
    render("home")


ft.run(main)
