import time
import asyncio
import streamlit as st

from fetcher import fetch_all as sequential_fetch
from async_fetcher import fetch_all as concurrent_fetch

st.set_page_config(page_title="Concurrent Data Fetcher", layout="wide")

st.title("⚡ Concurrent Data Fetcher Dashboard")

if st.button("Fetch Data"):

    col1, col2 = st.columns(2)

    # ---------------- Sequential ----------------
    with col1:
        st.subheader("Sequential Fetch")

        start = time.perf_counter()
        seq_data = sequential_fetch()
        seq_time = time.perf_counter() - start

        st.metric("Execution Time", f"{seq_time:.4f} sec")

        for key, value in seq_data.items():
            with st.expander(key):
                st.write(value)

    # ---------------- Concurrent ----------------
    with col2:
        st.subheader("Concurrent Fetch")

        start = time.perf_counter()
        async_data = asyncio.run(concurrent_fetch())
        async_time = time.perf_counter() - start

        st.metric("Execution Time", f"{async_time:.4f} sec")

        # If your async fetch returns a dictionary
        if isinstance(async_data, dict):
            for key, value in async_data.items():
                with st.expander(key):
                    st.write(value)

        # If your async fetch returns a list
        else:
            for i, value in enumerate(async_data, start=1):
                with st.expander(f"Result {i}"):
                    st.write(value)

    st.divider()

    st.subheader("Performance Comparison")

    saved = seq_time - async_time

    c1, c2, c3 = st.columns(3)

    c1.metric("Sequential", f"{seq_time:.4f} sec")
    c2.metric("Concurrent", f"{async_time:.4f} sec")
    c3.metric("Time Saved", f"{saved:.4f} sec")