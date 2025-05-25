from orchestrator import Orchestrator
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/activities",
    tags=["activities"]
)

async def get_orchestrator():
    return Orchestrator()

@router.get("/time_by_month")
async def plot_activity_time_by_month(
    months_back: int, 
    orch: Orchestrator = Depends(get_orchestrator)
):
    df = await orch.get_dataframe()
    summary = await orch.get_summary()
    chart = await orch.get_chart()

    table = summary.get_activity_time_by_month(df, months_back)
    img_base64 = chart.get_time_barchart(table)
    
    data_url = f"data:image/png;base64,{img_base64}"

    return JSONResponse(content={"image": data_url})

@router.get("/unique_days_by_month")
async def plot_activity_unique_days_by_month(
    months_back: int, 
    orch: Orchestrator = Depends(get_orchestrator)
):
    df = await orch.get_dataframe()
    summary = await orch.get_summary()
    chart = await orch.get_chart()

    table = summary.get_activity_unique_days_by_month(df, months_back)
    img_base64 = chart.get_unique_days_barchart(table)
    
    data_url = f"data:image/png;base64,{img_base64}"

    return JSONResponse(content={"image": data_url})

@router.get("/total_time_by_month")
async def total_time_by_month(
    months_back: int, 
    orch: Orchestrator = Depends(get_orchestrator)
):
    df = await orch.get_dataframe()
    summary = await orch.get_summary()
    chart = await orch.get_chart()

    table = summary.get_total_time_by_month(df, months_back)
    img_base64 = chart.get_total_time_barchart(table)
    
    data_url = f"data:image/png;base64,{img_base64}"

    return JSONResponse(content={"image": data_url})

@router.get("/total_unique_days_by_month")
async def total_unique_days_by_month(
    months_back: int, 
    orch: Orchestrator = Depends(get_orchestrator)
):
    df = await orch.get_dataframe()
    summary = await orch.get_summary()
    chart = await orch.get_chart()

    table = summary.get_total_unique_days_for_month(df, months_back)
    img_base64 = chart.get_total_unique_days_barchart(table)
    
    data_url = f"data:image/png;base64,{img_base64}"

    return JSONResponse(content={"image": data_url})