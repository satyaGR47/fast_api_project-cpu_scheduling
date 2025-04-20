from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from algorithm.fsfs import fcfs_scheduling
from algorithm.sjf import sjf_non_preemptive
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="template")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/schedule", response_class=HTMLResponse)
async def schedule(
    request: Request,
    pids: str = Form(...),
    arrivals: str = Form(...),
    bursts: str = Form(...),
    algorithm: str = Form(...)
):
    process_id_list = [pid.strip() for pid in pids.split(",")]
    arrival_time_list = list(map(int, arrivals.split(",")))
    burst_time_list = list(map(int, bursts.split(",")))

    processes = []
    for pid, arrival, burst in zip(process_id_list, arrival_time_list, burst_time_list):
        processes.append({
            "process_id": pid,
            "arrival_time": arrival,
            "burst_time": burst
        })

    if algorithm == "fcfs":
        scheduled_processes = fcfs_scheduling(processes)
        algorithm_name = "First Come First Serve (FCFS)"
    elif algorithm == "sjf":
        scheduled_processes = sjf_non_preemptive(processes)
        algorithm_name = "Shortest Job First (SJF)"

    else:
        return HTMLResponse(content="Invalid algorithm selected.", status_code=400)

    total_waiting_time = sum(p['waiting_time'] for p in scheduled_processes)
    average_waiting_time = total_waiting_time / len(scheduled_processes)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "processes": scheduled_processes,
        "average_waiting_time": round(average_waiting_time, 2),
        "algorithm": algorithm_name
    })



#TODO: Need to add more algorithm api like wise.
        






