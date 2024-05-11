
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor, SimpleSpanProcessor, ConsoleSpanExporter
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
        BatchSpanProcessor,
        ConsoleSpanExporter,
    )

from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.trace import Status, StatusCode


    # Creates a tracer from the global tracer provider
tracer = trace.get_tracer("my.tracer.name")
resource = Resource.create({"service.name": "WEB"})
provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

infrastackai = os.environ.get("infrastackai", "false").lower() == "true"
infrastackai_api_key = os.environ.get("infrastackai_api_key", "")

if infrastackai:

    # Adds span processor with the OTLP exporter to the tracer provider
    provider.add_span_processor(
        BatchSpanProcessor(OTLPSpanExporter(endpoint="https://collector-us1-http.infrastack.ai/v1/traces", headers=(("infrastack-api-key", infrastackai_api_key),)))
    )

