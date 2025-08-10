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
    include_this_month: bool,
    orch: Orchestrator = Depends(get_orchestrator)
):
    df_raw = await orch.get_dataframe()
    summary = await orch.get_summary()

    df = summary.get_activity_time_by_month(df_raw, months_back, include_this_month)
    df_json = summary.get_json(df)
    
    response_data = {
        'title': 'Total Time comparison by Activity Type',
        'ylabel': 'Total Time (hours)',
        'data': df_json
    }

    return JSONResponse(content=response_data)

@router.get("/unique_days_by_month")
async def plot_activity_unique_days_by_month(
    months_back: int, 
    include_this_month: bool,
    orch: Orchestrator = Depends(get_orchestrator)
):
    df_raw = await orch.get_dataframe()
    summary = await orch.get_summary()

    df = summary.get_activity_unique_days_by_month(df_raw, months_back, include_this_month)
    df_json = summary.get_json(df)
    
    response_data = {
        'title': 'Unique days comparison by Activity Type',
        'ylabel': 'Days',
        'data': df_json
    }

    return JSONResponse(content=response_data)

@router.get("/total_time_by_month")
async def total_time_by_month(
    months_back: int, 
    include_this_month: bool,
    orch: Orchestrator = Depends(get_orchestrator)
):
    df_raw = await orch.get_dataframe()
    summary = await orch.get_summary()

    df = summary.get_total_time_by_month(df_raw, months_back, include_this_month)
    df_json = summary.get_json(df)
    
    response_data = {
        'title': 'Total Time comparison by Months',
        'ylabel': 'Total Time (hours)',
        'data': df_json
    }

    return JSONResponse(content=response_data)

@router.get("/total_unique_days_by_month")
async def total_unique_days_by_month(
    months_back: int, 
    include_this_month: bool,
    orch: Orchestrator = Depends(get_orchestrator)
):
    df_raw = await orch.get_dataframe()
    summary = await orch.get_summary()

    df = summary.get_total_unique_days_for_month(df_raw, months_back, include_this_month)
    df_json = summary.get_json(df)
    
    response_data = {
        'title': 'Unique Days comparison by Months',
        'ylabel': 'Unique Days',
        'data': df_json
    }

    return JSONResponse(content=response_data)

@router.get("/top_three_activities")
async def top_three_activities_by_month(
    months_back: int, 
    include_this_month: bool,
    orch: Orchestrator = Depends(get_orchestrator)
):
    df_raw = await orch.get_dataframe()
    summary = await orch.get_summary()

    df = summary.get_top_three_activities_by_month(df_raw, months_back, include_this_month)
    response_data = summary.get_json(df)

    return JSONResponse(content=response_data)

@router.get("/top_three_categories")
async def top_three_categories_by_month(
    months_back: int, 
    include_this_month: bool,
    orch: Orchestrator = Depends(get_orchestrator)
):
    df_raw = await orch.get_dataframe()
    summary = await orch.get_summary()

    df = summary.get_top_three_categories_by_month(df_raw, months_back, include_this_month)
    response_data = summary.get_json(df)

    return JSONResponse(content=response_data)

@router.get("/average_time_per_day")
async def average_time_per_day(
    months_back: int, 
    include_this_month: bool,
    orch: Orchestrator = Depends(get_orchestrator)
):
    df_raw = await orch.get_dataframe()
    summary = await orch.get_summary()

    df = summary.get_average_time_per_day(df_raw, months_back, include_this_month)
    response_data = summary.get_json(df)

    return JSONResponse(content=response_data)

@router.get("/the_most_active_month")
async def the_most_active_month(
    orch: Orchestrator = Depends(get_orchestrator)
):
    df_raw = await orch.get_dataframe()
    summary = await orch.get_summary()

    df = summary.get_most_active_month(df_raw)
    response_data = summary.get_json(df)

    return JSONResponse(content=response_data)