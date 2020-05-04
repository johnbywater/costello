# Costello

[![Build Status](https://travis-ci.org/johnbywater/costello.svg?branch=master)](https://travis-ci.org/johnbywater/costello)
[![Coverage Status](https://coveralls.io/repos/github/johnbywater/costello/badge.svg?branch=master#)](https://coveralls.io/github/johnbywater/costello)

System to support mass contact tracing for infectious disease.

This system is motivated by the occurrence of the Cononavirus (COVID-19) pandemic.

## Abstract

*Costello* is a reliable, scalable, event-sourced, open source software system designed to support
mass contact tracing for novel infectious diseases such as the Cononavirus (COVID-19) virus. It is
being developed to support a need expressed many times by public health experts such as Anthony Costello,
Alison Pollock, Jeanelle de Gruchy and others, and public health institutions such as the World Health
Organisation, and the European Centre for Disease Prevention and Control.

## Background notes

* WHO Director-General's opening remarks at the media briefing on COVID-19 - 11 March 2020
  * "If countries detect, test, treat, isolate, trace, and mobilize their people in the response, those with a handful of cases can prevent those cases becoming clusters, and those clusters becoming community transmission. Even those countries with community transmission or large clusters can turn the tide on this virus. Several countries have demonstrated that this virus can be suppressed and controlled."
  * https://www.who.int/dg/speeches/detail/who-director-general-s-opening-remarks-at-the-media-briefing-on-covid-19---11-march-2020

* European Centre for Disease Prevention and Control - Contact tracing: Public health management of persons, including healthcare workers, having had contact with COVID-19 cases in the European Union
  * "This document outlines the key steps of contact tracing, including contact identification, listing and follow-up, in the context of the COVID-19 response. Contact management is based on the latest available evidence, as outlined below.
    * Current estimates suggest a median incubation period from five to six days, with a range from 1 to 14 days. A recent modelling study confirmed that it remains prudent to consider an incubation period of up to 14 days [1,2].
    * A case may already be infectious up to 48 hours before the onset of symptoms. A recent study reported that 12.6% of case reports indicated pre-symptomatic transmission [3]. In addition, the proportion of presymptomatic transmission has been inferred through modelling and was estimated to be – in the presence of control measures – at around 48% and 62% in Singapore and China (Tianjin data), respectively [4]. Other studies have shown no significant difference in viral load in asymptomatic and symptomatic patients, indicating the potential of virus transmission from asymptomatic patients [5-7].
    * Transmission is believed to be mainly via respiratory droplets and direct contact with infected people, andindirect contact with surfaces or objects in the immediate environment [8]. Recent experimental studies carried out under highly controlled conditions have demonstrated the survival of SARS-CoV-2 on different surfaces as well as in aerosol. Different levels of environmental contamination have been described in
rooms of COVID-19 patients [9-11].
    * Up to 10% of reported cases in China [12] and up to 9% of cases in Italy were among healthcare workers[13]. It is likely that nosocomial outbreaks play an important role in amplifying local outbreaks, and they disproportionately affect elderly and vulnerable populations." 
  * https://www.ecdc.europa.eu/en/covid-19-contact-tracing-public-health-management

* Really important discussion about contact tracing on World At One today (22nd April 2020), with Daniel Falush (https://twitter.com/DanielFalush) and Allyson Pollock (https://theconversation.com/profiles/allyson-pollock-124791)
  * https://www.bbc.co.uk/programmes/m000hfrh (30:27 in)
  * evolve lockdown
  * not everyone needs to be tasted
  * temperature checking as first way of detection
  * easier when everyone's on lockdown (one of reasons for lockdown)
  * do you need an app, not essential in China, have used teams of tracers
Allyson (absolutely stunning amount of useful information and clarity, almost a blue print that we perhaps should just follow):
  * have been doing it for hundreds of years, essential mechanism, nothing new
  * what is new is that govt has taken out local capacity to do contact tracing, through Health and Social Care Act 2012, and through austerity reforms, communicable disease Control taken out of local health authorities and local authorities
  * great deal of expertise in this country
  * we don't need fancy expensive apps, where people are going to be exposed to issues of data privacy
  * should be following San Francisco model, use people and telephones
  * local practical solutions with lots of local data
  * national epidemic made up of hundreds of small outbreaks
  * so you have to get on top of these small outbreaks, and know your area, and have teams and teams of people on the telephone monitoring people
  * not rocket science
  * 750000 people volunteered for NHS not being used
  * in Ireland they are using teachers and barristers and students
  * we have armies of people, including the army, and at local level they can decide what they want to do
  * it's beginning to happen, Welsh Assembly, local government association is going to work with Welsh Assembly to do contact tracing
  * we have lots of examples from around the world
  * also have lots of really good advice from European Centre for Disease Prevention and Control, have been updating their technical reports
  * if we had done this in nursing homes we wouldn't have seen nearly there number of deaths that we are seeing now
  * digital tracking has real data privacy issues, that's why it's not being used in high tech centre like San Francisco, we need technology, telephones and digital recording of data to feedback to local level as well as Public Health England
  * the big problem is this local capacity
  * should not be over emphasizing importance of digital apps or testing, clinical observation picks up more cases
  * need to be focussing on getting basics right
  * environmental health officers have been asking why they haven't been asked to do this
  * 343 local authorities, they need to be empowered along with their directors of public health to do this, they could do it very quickly, training up volunteers, with training courses over one two or three days, and this could be done within five days
  * start with areas with low case numbers, happening already in Sheffield and Wales
  * government worries me greatly because it has been taking centralized approach, which has been the big problem in handling this epidemic
  * epidemics can only be tackled if you know your local areas and know your local outbreaks
  * government needs to do much more devolution and putting resources back into local government and local health bodies 

* Letter from Richard Gleave, Deputy Chief Executive, Public Health England to  Directors of Public Health (24 April 2020)
  * "There will be a national-level recruitment initially of around 18,000 staff (around 3,000 qualified public health and clinical professionals and around 15,000 call handlers) to undertake the phone-based contact tracing with both the cases and the contacts. We are planning on the basis that the service will ramp up quickly. These staff will work under the leadership of the PHE-led national function working alongside an external logistics partner and we are exploring the regional and local footprints that will enable the service to link with local community support to people who need to self-isolate."
  * https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/881231/Letter_to_DsPH_on_contact_tracing.pdf

* Dr Jeanelle de Gruchy (director of public health for Tameside, president of association of directors of public health) on Today programme this morning (25th April 2020), with Prof Azeem Majheed head of dept of primary care and public health at Imperial College
  * https://www.bbc.co.uk/programmes/m000hmyy (18:30 in)
  * https://www.england.nhs.uk/author/dr-jeanelle-de-gruchy/
  * https://www.imperial.ac.uk/people/a.majeed
  * Presenter said: [repeating govt lines] "Health Sec told us 18,000 contact tracers operating in a few weeks to identify all those in contact with confirmed cases of the virus is what should lead to a more precise understand of its spread [rather than about working towards eradication]
  * de Gruchy said she is wanting to contribute to design of contact tracing scheme (but not really feeling like she has been or will be involved)
  * talked about need for process that is integrated / coherent with the testing process and also supported quarantine
  * that this depends on local knowledge [which feels obvious, but I'm not really sure what this actually means in reality  * I guess you need to have local contact?]
  * asked about how intrusive it will be, said that it's a matter of getting telephone numbers off people who are considered to be infected (which assumed
  * probably need 50000 contact tracers for England, so we can get on top of virus and bring it under control
  * need to work under people who are more experience
  * talking about contact tracing being something that is easily trained, people follow script on a computer screen, and are prompted about what to say
  * would it be useful to be doing it right now? Health Sec said it's effective only if numbers are lower [zzzzz]
  * we need to get the numbers we need right now, was mistake to stop in March, have lost a month
  * how intrusive? call centre phase, but also 3000 people more trained to have more detailed conversations, then talk to contacts, tell them they've been in contact and advise them what to do, will be asking people to self-isolate, local knowledge so important for vulnerable and live alone, understand how this lands in people's lives, need that knowledge to inform design of national programme
  * https://twitter.com/ADPHUK/status/1253939508229410817
  * https://twitter.com/Jeanelleuk/status/1253934894608244736
  * https://twitter.com/jimmcmanusph/status/1253959644499804160
  * https://twitter.com/AllysonPollock/status/1253972451245031426
  * https://twitter.com/profchrisham/status/1253935451142053892
  * https://twitter.com/JimBethell/status/1253988671356837888

* Wikipedia article on contact tracing and digital contract tracing
  * https://en.wikipedia.org/wiki/Contact_tracing
  * https://en.wikipedia.org/wiki/Digital_contact_tracing

## Other projects

To name just a few...

* WHO Go.Data tool https://www.who.int/godata
* NextTrace https://nexttrace.org/
  * NextTrace "white paper" https://docs.google.com/document/d/1inQyAzC8eihq2kCz487Xb7dkjNaWtM3uzL_ceNrgpXI/edit
* TraceTogether https://en.wikipedia.org/wiki/TraceTogether
* OpenTrace https://en.wikipedia.org/wiki/BlueTrace#OpenTrace
* Google/Apple contract tracing project https://en.wikipedia.org/wiki/Google_/_Apple_contact_tracing_project
* Decentralized Privacy-Preserving Proximity Tracing https://github.com/DP-3T

...and many more.

## Stories

* Kerela https://www.theguardian.com/commentisfree/2020/apr/21/kerala-indian-state-flattened-coronavirus-curve
* Agra https://uk.reuters.com/article/us-health-coronavirus-india-agra-insight/in-the-city-of-the-taj-mahal-coronavirus-resurgence-carries-warning-signs-idUKKBN22G08I
 
## Analysis

Contact tracing is an important part of the process of disease eradication and control ("detect, test, treat, isolate,
trace, and mobilize"). A fine balance must be found and maintained between protecting health, minimizing economic
and social disruption, and respecting human rights.

Just as a pandemic is made up of epidemics in many countries around the world, an epidemic is made up of
many outbreaks around a country. It is necessary to tackle a pandemic by tackling outbreaks at a local level. 

Contact tracing is intended to catch up with the spread of an infectious disease by identifying individuals
that may have been infected by exposure to an infectious individual. The related parts are intended variously
to find suspected cases of infection ("detect"), to confirm suspected cases of infection ("test"), to mitigate
the effects of the disease on an individual ("treat"), to inhibit the further spread of the disease by quarantining
suspected cases and providing support for their needs ("isolate"), and to encourage engagement with and contributions
to the process of disease control such as with detecting, testing, treating, tracing, isolating, and mobilizing
("mobilize").

There are various approaches to contract tracing. The "traditional" approach establishes contract tracing teams to
interview "confirmed cases", generating a list of "contacts" which are classed as "high risk" and "low risk". High
risk contacts are normally quarantined and tested. Low risk contacts are advised to avoid travel and contact with
vulnerable people, and may be tested. Both types of contact are monitored for the development of symptoms. A
positive test or development of symptoms may cause a contact to be considered as a "confirmed case".

The "digital" contract tracing approach uses proximity detection features of digital devices to log contact events,
and the log of contact events is used to notify contacts of confirmed cases.

The approach taken in this project is to build on both these approaches and to go further by adopting a probabilistic
approach to managing risk and optimising outcomes, based on current understandings of transmission, development and
duration of infectiousness, development and duration of symptoms, and sensitivity and specificity
of tests of different kinds, so that available resources can be used most effectively.

This project's approach to development follows established open source licensing, and
approaches to development of reliable, scalable, maintainable distributed software
systems such as domain driven design and event sourcing.

## Scope of the work

- Contact tracing work
    - Open new suspected case of infection
        - Add personal information
            - Name
            - Telephone number
        - Record reason for opening case
            - Positive test result
                - Test reference number
                - Type of test
                - Date of test
            - Matching symptoms
                - Date of onset of symptoms
                - Notes
            - Contact with suspected case
                - Case ID
        - Notes
    - Select suspected case of infection
        - By case ID
        - By priority for investigation
        - By telephone number
        - By test request ID
    - Interview suspected case of infection
        - Record time of interview
        - Ask about and assess encounters with other people
        - Record details of each encounter
            - Place
            - Date and time
            - Type of encounter
            - Risk of transmission
            - Name of person
            - Telephone number of person
        - Ask about use of shared spaces (work, public transport, shops, gyms, restaurants, etc)
        - Record details of each use
            - Place
            - Date and time
            - Type of use
            - Risk of transmission
        - Ask about symptoms
        - Record symptoms
        - Give advice and instructions
            - Avoid infecting other people
                - Quarantine requirements
                - Wear a mask during encounters with others
                - Avoid meeting vulnerable people
                - Avoid using shared spaces
            - Monitor symptoms and request medical assistance if required
                - Temperature, coughing, breathing, oxygen levels
            - Start recording encounters with other people
        - Record advice and instructions given
        - Schedule follow up interview
        - Open new suspected cases of infection...
    - Investigate other users of a shared space
        - Identify people who shared space at the same time or afterwards
        - Ask about and assess encounters with other people
            - From memory
            - Log in venue or transport vehicle
            - Details of each encounter
                - Place
                - Date and time
                - Type of encounter
                - Risk of transmission
                - Name of person
                - Telephone number of person
            - Open new suspected cases of infection...
    - Request test for suspected case of infection
    - Update suspected case with test result
    - Close suspected case of infection
        - Record reason for closing case


Need to register who went into a shared spaces so can contact trace?
Need to investigate use of shops (payment card information?)
Need model relating earliest time of infectiousness to:
   - first positive test result (14 days before?)
   - onset of matching symptoms (14 days before?)
   - contact with suspected case of infection (2/3 days later?)


## Scope of the system

* Aggregate: SuspectedCase
  * Domain events:
      * Opened
      * Closed
      * NamedUpdated
      * TelephoneNumberUpdated
      * EmailAddressUpdated
      * InterviewNotesAdded
      * InterviewNotesUpdated
      * TestRequested
      * TestResultsReceived
      * SymptomsReported
      * IndividualEncountered
      * PlaceVisited
      * TransportUsed
      * QuarantineStatusUpdated
  
* Aggregate: Disease
  * Domain events:
      * Registered
      * InfectiousProfileUpdated
      * SymptomDevelopmentProfileUpdated
 
* Aggregate: Test
  * Created
  * MethodUpdated
  * SensitivityProfileUpdated
  * SpecificityProfileUpdated

* Aggregate: ContractTracingWorker
  * Created
  * ProfileUpdated
  * CaseSelected
  * CaseDeselected
